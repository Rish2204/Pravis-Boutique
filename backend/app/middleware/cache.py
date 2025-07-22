import os
import json
import hashlib
import asyncio
from functools import wraps
from typing import Callable, Optional, Dict, Any, Union
from fastapi import Request, Response
import aioredis
from app.core.config import settings

# Redis connection
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_pool = None

async def get_redis_pool():
    """Get or create Redis connection pool"""
    global redis_pool
    if redis_pool is None:
        redis_pool = await aioredis.create_redis_pool(redis_url)
    return redis_pool

async def close_redis_pool():
    """Close Redis connection pool"""
    global redis_pool
    if redis_pool is not None:
        redis_pool.close()
        await redis_pool.wait_closed()
        redis_pool = None

def generate_cache_key(request: Request, prefix: str = "api-cache") -> str:
    """Generate a unique cache key based on request parameters"""
    # Create a unique cache key based on:
    # 1. Full URL path
    # 2. Query parameters
    # 3. Request body (if available)
    key_parts = [request.url.path]
    
    # Add query parameters
    if request.query_params:
        key_parts.append(str(request.query_params))
    
    # Add request body if available and not too large
    if hasattr(request, "body") and request.body:
        try:
            # Only include body for smaller payloads
            if len(request.body) < 1024:  # 1KB limit
                key_parts.append(request.body.decode())
        except:
            pass
    
    # Create MD5 hash of the combined string
    key_string = "".join(key_parts)
    key_hash = hashlib.md5(key_string.encode()).hexdigest()
    
    return f"{prefix}:{key_hash}"

async def cache_response(
    request: Request,
    response: Response,
    ttl: int = 300,  # Default TTL: 5 minutes
    prefix: str = "api-cache"
) -> None:
    """Store response in Redis cache"""
    # Only cache successful responses
    if response.status_code != 200:
        return
    
    # Don't cache very large responses
    response_body = b""
    for chunk in response.body_iterator:
        response_body += chunk
    
    if len(response_body) > 1024 * 100:  # 100KB limit
        # Reset the response body
        response.body = response_body
        return
    
    # Generate cache key
    cache_key = generate_cache_key(request, prefix)
    
    # Cache response with metadata
    cache_data = {
        "status_code": response.status_code,
        "content_type": response.headers.get("content-type"),
        "body": response_body.decode("utf-8") if response_body else "",
    }
    
    # Store in Redis
    pool = await get_redis_pool()
    await pool.setex(cache_key, ttl, json.dumps(cache_data))
    
    # Reset the response body
    response.body = response_body

class CacheMiddleware:
    """Middleware for caching API responses in Redis"""
    
    def __init__(self, app: Any, ttl: int = 300):
        self.app = app
        self.ttl = ttl
    
    async def __call__(self, scope: Dict, receive: Callable, send: Callable) -> None:
        if scope["type"] != "http" or scope["method"] != "GET":
            await self.app(scope, receive, send)
            return
            
        # Create a request object from scope
        request = Request(scope)
        
        # Continue with middleware logic
        async def _call_next(request):
            # Workaround: we need to create a new scope with the request
            _receive = receive
            response_sent = [False]
            response_body = []
            
            async def _send(message):
                if message["type"] == "http.response.start":
                    response_sent[0] = True
                elif message["type"] == "http.response.body":
                    response_body.append(message.get("body", b""))
                await send(message)
            
            # Call the next middleware/app
            await self.app(scope, _receive, _send)
            
            # Construct a response for our cache logic
            return Response(b"".join(response_body))
            
        # The rest of the caching logic from the original implementation
        # would go here, using the wrapped _call_next and our adapted scope
        
        # For now, just pass through without caching to fix the error
        await self.app(scope, receive, send)
        # Skip caching for non-GET requests
        if request.method != "GET":
            return await call_next(request)
        
        # Generate cache key
        cache_key = generate_cache_key(request)
        
        # Try to get from cache
        pool = await get_redis_pool()
        cached = await pool.get(cache_key)
        
        if cached:
            try:
                # Parse cached response
                cache_data = json.loads(cached)
                
                # Create response from cache
                response = Response(
                    content=cache_data["body"],
                    status_code=cache_data["status_code"],
                    media_type=cache_data["content_type"]
                )
                
                # Add cache header
                response.headers["X-Cache"] = "HIT"
                return response
                
            except Exception as e:
                # Log the error but continue with normal request
                print(f"Cache retrieval error: {str(e)}")
        
        # Process the request normally
        response = await call_next(request)
        
        # Cache the response (only if it's a successful response)
        if response.status_code == 200:
            asyncio.create_task(cache_response(request, response, self.ttl))
            
            # Mark as cache miss
            response.headers["X-Cache"] = "MISS"
        
        return response

def cached(ttl: int = 300):
    """Decorator for caching endpoint responses"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Find request object
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
            
            if not request:
                for _, value in kwargs.items():
                    if isinstance(value, Request):
                        request = value
                        break
            
            if not request or request.method != "GET":
                # If no request found or not a GET, just execute the function
                return await func(*args, **kwargs)
            
            # Generate cache key
            cache_key = generate_cache_key(request)
            
            # Try to get from cache
            pool = await get_redis_pool()
            cached = await pool.get(cache_key)
            
            if cached:
                try:
                    # Parse cached response
                    cache_data = json.loads(cached)
                    
                    # Create response from cache
                    response = Response(
                        content=cache_data["body"],
                        status_code=cache_data["status_code"],
                        media_type=cache_data["content_type"]
                    )
                    
                    # Add cache header
                    response.headers["X-Cache"] = "HIT"
                    return response
                    
                except Exception as e:
                    # Log the error but continue with normal execution
                    print(f"Cache retrieval error: {str(e)}")
            
            # Execute the function
            response = await func(*args, **kwargs)
            
            # Cache the response if possible
            if hasattr(response, "status_code") and response.status_code == 200:
                asyncio.create_task(cache_response(request, response, ttl))
                
                # Mark as cache miss
                response.headers["X-Cache"] = "MISS"
            
            return response
        
        return wrapper
    
    return decorator
