import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.monitoring import setup_azure_monitoring
from app.api.api_v1.api import api_router
from app.middleware.error_handlers import register_exception_handlers
from app.middleware.logging import setup_logging
from app.middleware.rate_limiter import add_rate_limiter
# from app.middleware.cache import CacheMiddleware  # Temporarily disabled for Python 3.12

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for Pravis Boutique e-commerce platform",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/", response_model=dict)
def read_root() -> dict:
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Pravis Boutique API", 
        "version": "1.0.0",
        "docs": "/docs",
        "environment": settings.ENVIRONMENT
    }

# Register exception handlers
register_exception_handlers(app)

# Setup logging middleware
setup_logging(app)

# Add rate limiting middleware
add_rate_limiter(app)

# Add Redis caching middleware (temporarily disabled)
# app.add_middleware(CacheMiddleware, ttl=300)  # Cache GET responses for 5 minutes

# Setup Azure monitoring (Application Insights and Log Analytics)
if settings.ENVIRONMENT != "development":
    setup_azure_monitoring(app)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)
