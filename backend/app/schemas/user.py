"""
Pydantic schemas for User model
"""
from datetime import datetime
from typing import Optional, Dict, Any

from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    """Base schema for User"""
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    """Schema for creating a new User"""
    password: str

    @validator('password')
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v


class UserUpdate(BaseModel):
    """Schema for updating a User"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    preferences: Optional[Dict[str, Any]] = None

    @validator('password')
    def password_min_length(cls, v):
        if v is not None and len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v


class UserInDBBase(UserBase):
    """Base schema for User in DB"""
    id: int
    created_at: datetime
    preferences: Dict[str, Any] = {}

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """Response schema for User"""
    pass


class UserInDB(UserInDBBase):
    """Schema for User in DB with hashed_password"""
    hashed_password: str
