from fastapi import APIRouter

# Import router from endpoints
from app.api.api_v1.endpoints import health, auth, ai_analytics
# Add other endpoint imports as needed: items, users, etc.

api_router = APIRouter()

# Include routers from endpoints
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(ai_analytics.router, prefix="/ai-analytics", tags=["ai", "analytics"])
# Add other routers as needed
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
