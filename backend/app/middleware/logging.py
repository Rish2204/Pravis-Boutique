import time
import logging
import uuid
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for logging request and response details.
    Adds a unique request ID to each request for traceability.
    """
    
    def __init__(self, app: ASGIApp):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next):
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        
        # Add request ID to request state
        request.state.request_id = request_id
        
        # Start timer
        start_time = time.time()
        
        # Log request details (skip for common endpoints that return 200)
        if not (request.url.path in ["/", "/api/v1/health/"] and request.method == "GET"):
            logger.info(
                f"Request started: {request.method} {request.url.path} "
                f"(ID: {request_id})"
            )
        
        # Process request and get response
        try:
            response = await call_next(request)
            
            # Calculate processing time
            process_time = time.time() - start_time
            
            # Add custom headers
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time)
            
            # Log response details (skip 200 OK responses, highlight errors)
            if response.status_code != 200:
                log_level = logger.error if response.status_code >= 500 else logger.info
                log_level(
                    f"Request completed: {request.method} {request.url.path} "
                    f"- Status: {response.status_code} - Time: {process_time:.4f}s "
                    f"(ID: {request_id})"
                )
            
            return response
        except Exception as e:
            # Log exceptions
            process_time = time.time() - start_time
            logger.error(
                f"Request failed: {request.method} {request.url.path} "
                f"- Error: {str(e)} - Time: {process_time:.4f}s "
                f"(ID: {request_id})"
            )
            raise


def setup_logging(app: FastAPI) -> None:
    """Set up request logging middleware."""
    app.add_middleware(RequestLoggingMiddleware)
