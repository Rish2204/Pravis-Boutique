from pydantic import BaseModel, Field
from typing import Optional


class HealthResponse(BaseModel):
    """Schema for health check response."""
    status: str = Field(..., description="API status")
    version: str = Field(..., description="API version")
    api: str = Field(..., description="API name")
    environment: str = Field(..., description="Deployment environment")


class DatabaseHealthResponse(BaseModel):
    """Schema for database health check response."""
    status: str = Field(..., description="Status of the database connection")
    database: str = Field(..., description="Connection status")
    detail: Optional[str] = Field(None, description="Error details if any")
