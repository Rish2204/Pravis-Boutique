from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    username: str
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for user creation."""
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """Schema for user updates."""
    email: EmailStr = None
    username: str = None
    password: str = Field(None, min_length=8)


class UserInDB(UserBase):
    """Schema for user in database."""
    id: int
    hashed_password: str

    class Config:
        orm_mode = True


class User(UserBase):
    """Schema for user response."""
    id: int

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    """Schema for login request."""
    username: str
    password: str


class TokenResponse(BaseModel):
    """Schema for token response."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user_id: str
