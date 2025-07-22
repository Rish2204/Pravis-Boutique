from typing import Generator, Optional, Dict, Any

from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.config import settings
from app.core.auth import get_current_user as auth_get_current_user

# Database dependency - will be used in routes that need database access
def get_db_session() -> Generator[Session, None, None]:
    """
    Returns a database session that can be used in route functions.
    Will automatically close the session when the request is finished.
    """
    return get_db()

# Security dependencies for protected routes
async def get_current_user(db: Session = Depends(get_db_session)) -> Dict[str, Any]:
    """
    Get the current authenticated user using JWT.
    """
    # Use the core auth function
    current_user = await auth_get_current_user()
    
    # In a real app, you might want to verify the user exists in the database
    # and fetch the complete user object
    return current_user

# Role-based dependencies
async def get_current_admin_user(current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    """
    Check if the current user has admin privileges.
    """
    # Check if user has admin role
    is_admin = current_user.get("role") == "admin"
    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user


async def get_current_active_user(current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    """
    Check if the current user is active.
    """
    if current_user.get("is_active") is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )
    return current_user


async def get_current_active_superuser(current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    """
    Check if the current user is active and a superuser.
    """
    if current_user.get("is_active") is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )
    if current_user.get("is_superuser") is not True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
        )
    return current_user


# Request context utilities
def get_request_id(request: Request) -> str:
    """
    Get the request ID from the request state.
    Useful for correlating logs and tracking request flow.
    """
    return getattr(request.state, "request_id", "unknown")
