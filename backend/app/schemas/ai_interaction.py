"""
Pydantic schemas for AI interaction models.
These schemas define the structure for request and response data related to AI interactions.
"""

from pydantic import BaseModel, Field, validator
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from enum import Enum

from app.schemas.base import DateTimeModelMixin, IDModelMixin


class InteractionType(str, Enum):
    """Types of AI interactions that can be logged."""
    TRANSCRIPTION = "transcription"
    TEXT_TO_SPEECH = "tts"
    CHAT = "chat"
    RECOMMENDATION = "recommendation"
    SEARCH = "search"
    CUSTOM = "custom"


class AIInteractionBase(BaseModel):
    """Base schema for AI interactions."""
    interaction_type: InteractionType
    request_text: Optional[str] = None
    session_id: str
    context: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    model_name: Optional[str] = None
    model_version: Optional[str] = None


class AIInteractionCreate(AIInteractionBase):
    """Schema for creating a new AI interaction record."""
    user_id: Optional[int] = None
    client_ip: Optional[str] = None
    user_agent: Optional[str] = None


class AIInteractionUpdate(BaseModel):
    """Schema for updating an AI interaction record."""
    response_text: Optional[str] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[float] = None
    tokens_input: Optional[int] = None
    tokens_output: Optional[int] = None
    success: Optional[bool] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None


class AIInteractionInDB(AIInteractionBase, IDModelMixin, DateTimeModelMixin):
    """Schema for AI interaction data as stored in the database."""
    user_id: Optional[int] = None
    client_ip: Optional[str] = None
    user_agent: Optional[str] = None
    response_text: Optional[str] = None
    started_at: datetime
    completed_at: Optional[datetime] = None
    duration_ms: Optional[float] = None
    tokens_input: Optional[int] = None
    tokens_output: Optional[int] = None
    success: bool = True
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    user_rating: Optional[int] = None
    user_feedback: Optional[str] = None
    
    class Config:
        orm_mode = True


class AIInteractionResponse(AIInteractionInDB):
    """Schema for AI interaction response with computed fields."""
    total_tokens: Optional[int] = None
    
    @validator("total_tokens", always=True)
    def compute_total_tokens(cls, v, values):
        """Compute total tokens from input and output tokens."""
        input_tokens = values.get("tokens_input") or 0
        output_tokens = values.get("tokens_output") or 0
        return input_tokens + output_tokens


class AIFeedbackBase(BaseModel):
    """Base schema for AI feedback."""
    interaction_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    category: Optional[str] = None


class AIFeedbackCreate(AIFeedbackBase):
    """Schema for creating a new AI feedback record."""
    user_id: Optional[int] = None


class AIFeedbackUpdate(BaseModel):
    """Schema for updating an AI feedback record."""
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = None
    category: Optional[str] = None
    sentiment_score: Optional[float] = Field(None, ge=-1.0, le=1.0)
    tags: Optional[List[str]] = None
    reviewed: Optional[bool] = None
    reviewer_notes: Optional[str] = None


class AIFeedbackInDB(AIFeedbackBase, IDModelMixin, DateTimeModelMixin):
    """Schema for AI feedback data as stored in the database."""
    user_id: Optional[int] = None
    sentiment_score: Optional[float] = None
    tags: Optional[List[str]] = None
    reviewed: bool = False
    reviewer_notes: Optional[str] = None
    
    class Config:
        orm_mode = True


class AIFeedbackResponse(AIFeedbackInDB):
    """Schema for AI feedback response with additional information."""
    pass


class AIFeedbackSummary(BaseModel):
    """Summary statistics for AI feedback."""
    total_feedback: int
    average_rating: float
    rating_distribution: Dict[int, int]  # Map of rating value to count
    sentiment_distribution: Dict[str, int]  # Map of sentiment category to count
    common_tags: List[Dict[str, Union[str, int]]]  # List of tag name and count
    recent_comments: List[Dict[str, Any]]  # List of recent feedback with comments


class AIInteractionStats(BaseModel):
    """Statistics about AI interactions."""
    total_interactions: int
    successful_interactions: int
    failed_interactions: int
    average_duration_ms: float
    interaction_types: Dict[str, int]  # Map of interaction type to count
    average_tokens: Dict[str, float]  # Map of token type to average count
    success_rate_by_model: Dict[str, float]  # Map of model name to success rate
