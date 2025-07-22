from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db_session, get_current_user
from app.core.auth import create_access_token, verify_password
from app.core.config import settings
from app.schemas.auth import TokenResponse, User, LoginRequest

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login_access_token(
    db: Session = Depends(get_db_session),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    This endpoint follows the OAuth2 specification.
    """
    # In a real application, you would authenticate against your database
    # For now, we'll just use a hardcoded test user
    
    # Mock authentication - replace with actual DB authentication
    if form_data.username != "testuser" or not verify_password(form_data.password, "$2b$12$6HbRlKZQFqRYKQX6NOUKvepN0w0Y3gXBw32nNqXnNkcfnO5Q8r34q"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token with a specified expiry time
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Get user ID (in a real app, this would come from your user database)
    user_id = "1"  # Mock user ID
    
    # Create the JWT token
    access_token = create_access_token(
        subject=user_id, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # in seconds
        "user_id": user_id
    }


@router.post("/login/json", response_model=TokenResponse)
async def login_json(
    login_request: LoginRequest,
    db: Session = Depends(get_db_session)
) -> Any:
    """
    JSON login endpoint, alternative to the OAuth2 flow.
    """
    # In a real application, you would authenticate against your database
    # This is similar to the OAuth endpoint but accepts JSON instead of form data
    
    # Mock authentication - replace with actual DB authentication
    if login_request.username != "testuser" or not verify_password(login_request.password, "$2b$12$6HbRlKQFqRYKQX6NOUKvepN0w0Y3gXBw32nNqXnNkcfnO5Q8r34q"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # Create access token with a specified expiry time
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Get user ID (in a real app, this would come from your user database)
    user_id = "1"  # Mock user ID
    
    # Create the JWT token
    access_token = create_access_token(
        subject=user_id, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # in seconds
        "user_id": user_id
    }


@router.get("/me", response_model=User)
async def read_users_me(current_user: dict = Depends(get_current_user)) -> Any:
    """
    Get current user information.
    """
    # Convert dict to User object
    # In a real application, you would return the actual user from the database
    return User(
        id=int(current_user["id"]),
        email="test@example.com",
        username=current_user["username"],
        is_active=True
    )
