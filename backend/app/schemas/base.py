from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime

T = TypeVar('T')


class HTTPError(BaseModel):
    """Base model for HTTP error responses."""
    detail: str = Field(..., description="Error details")
    code: Optional[str] = Field(None, description="Error code for API consumers")


class ValidationError(BaseModel):
    """Model for validation errors."""
    loc: List[str] = Field(..., description="Error location")
    msg: str = Field(..., description="Error message")
    type: str = Field(..., description="Error type")


class HTTPValidationError(BaseModel):
    """Model for HTTP validation errors."""
    detail: List[ValidationError] = Field(..., description="List of validation errors")


class ResponseBase(GenericModel, Generic[T]):
    """Base model for standard API responses."""
    success: bool = Field(True, description="Success status")
    message: Optional[str] = Field(None, description="Response message")
    data: Optional[T] = Field(None, description="Response data")


class PaginatedResponseBase(ResponseBase, Generic[T]):
    """Base model for paginated API responses."""
    total: int = Field(..., description="Total number of items")
    page: int = Field(..., description="Current page number")
    size: int = Field(..., description="Page size")
    pages: int = Field(..., description="Total number of pages")
    data: List[T] = Field([], description="Page items")


class IDModelMixin(BaseModel):
    """Mixin for models with ID field."""
    id: int = Field(..., description="Unique identifier")


class DateTimeModelMixin(BaseModel):
    """Mixin for models with created_at and updated_at fields."""
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
