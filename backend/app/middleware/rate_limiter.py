import time
from typing import Dict, Tuple, Callable
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from fastapi.responses import JSONResponse
from app.schemas.base import HTTPError


class RateLimiter(BaseHTTPMiddleware):
    """
    Rate limiting middleware to prevent abuse of the API.
    Uses a simple sliding window algorithm.
    """
    
    def __init__(
        self,
        app: ASGIApp,
        rate_limit_per_minute: int = 60,
        exclude_paths: list = None
    ):
        super().__init__(app)
        self.rate_limit = rate_limit_per_minute
        self.window_size = 60  # 1 minute in seconds
        self.clients: Dict[str, list] = {}  # Store client request timestamps
        self.exclude_paths = exclude_paths or ["/api/v1/health", "/docs", "/redoc", "/openapi.json"]
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Skip rate limiting for excluded paths
        if any(request.url.path.startswith(path) for path in self.exclude_paths):
            return await call_next(request)
        
        # Get client identifier (IP address or API key if available)
        client_id = self._get_client_id(request)
        
        # Check if client is rate limited
        is_rate_limited, retry_after = self._is_rate_limited(client_id)
        
        if is_rate_limited:
            return JSONResponse(
                status_code=429,
                content=HTTPError(
                    detail="Too many requests",
                    code="rate_limit_exceeded"
                ).dict(),
                headers={"Retry-After": str(retry_after)}
            )
        
        # Client is not rate limited, proceed with the request
        return await call_next(request)
    
    def _get_client_id(self, request: Request) -> str:
        """Get a unique identifier for the client."""
        # First try to get API key from header if authentication is used
        api_key = request.headers.get("X-API-Key")
        if api_key:
            return f"apikey:{api_key}"
        
        # Otherwise use client IP address
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        
        return request.client.host
    
    def _is_rate_limited(self, client_id: str) -> Tuple[bool, int]:
        """
        Check if a client is rate limited.
        Returns a tuple of (is_rate_limited, retry_after).
        """
        current_time = time.time()
        
        # Initialize client record if it doesn't exist
        if client_id not in self.clients:
            self.clients[client_id] = []
        
        # Remove timestamps outside the current window
        self.clients[client_id] = [
            ts for ts in self.clients[client_id]
            if ts > current_time - self.window_size
        ]
        
        # Check if client has exceeded rate limit
        if len(self.clients[client_id]) >= self.rate_limit:
            # Calculate retry after time
            oldest_timestamp = min(self.clients[client_id])
            retry_after = int(oldest_timestamp + self.window_size - current_time)
            return True, retry_after
        
        # Client is not rate limited, add current timestamp
        self.clients[client_id].append(current_time)
        return False, 0


def add_rate_limiter(app: FastAPI, rate_limit: int = 60) -> None:
    """Add rate limiting middleware to the FastAPI app."""
    app.add_middleware(RateLimiter, rate_limit_per_minute=rate_limit)
