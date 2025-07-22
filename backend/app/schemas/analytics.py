"""
Pydantic schemas for analytics models
"""
from datetime import datetime
from typing import Optional, Dict, Any, List

from pydantic import BaseModel


class AnalyticsEventBase(BaseModel):
    """Base schema for AnalyticsEvent"""
    event_type: str
    user_id: Optional[int] = None
    event_data: Dict[str, Any] = {}


class AnalyticsEventCreate(AnalyticsEventBase):
    """Schema for creating a new AnalyticsEvent"""
    pass


class AnalyticsEventInDB(AnalyticsEventBase):
    """Schema for AnalyticsEvent in DB"""
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True


class VoiceInteractionBase(BaseModel):
    """Base schema for VoiceInteraction"""
    user_id: Optional[int] = None
    query: str
    response: str
    metadata: Dict[str, Any] = {}
    is_successful: bool = True
    session_id: Optional[str] = None


class VoiceInteractionCreate(VoiceInteractionBase):
    """Schema for creating a new VoiceInteraction"""
    pass


class VoiceInteractionInDB(VoiceInteractionBase):
    """Schema for VoiceInteraction in DB"""
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True


class UserSessionBase(BaseModel):
    """Base schema for UserSession"""
    session_id: str
    user_id: Optional[int] = None
    is_active: bool = True
    device_info: Dict[str, Any] = {}
    ip_address: Optional[str] = None


class UserSessionCreate(UserSessionBase):
    """Schema for creating a new UserSession"""
    pass


class UserSessionUpdate(BaseModel):
    """Schema for updating a UserSession"""
    ended_at: Optional[datetime] = None
    is_active: Optional[bool] = None


class UserSessionInDB(UserSessionBase):
    """Schema for UserSession in DB"""
    id: int
    started_at: datetime
    ended_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class AnalyticsReport(BaseModel):
    """Schema for analytics reports"""
    total_events: int
    events_by_type: Dict[str, int]
    events_by_day: Dict[str, int]
    
    
class VoiceInteractionMetrics(BaseModel):
    """Schema for voice interaction metrics"""
    total_interactions: int
    successful_interactions: int
    average_query_length: float
    interactions_by_day: Dict[str, int]
