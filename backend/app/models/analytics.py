"""
Analytics data models for tracking user interactions and voice agent events
"""
from datetime import datetime
from typing import Dict, Any, Optional

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship

from app.db.session import Base


class AnalyticsEvent(Base):
    """Model for tracking general analytics events"""
    __tablename__ = "analytics_events"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String(50), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    event_data = Column(JSON, nullable=False, default={})
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    
    # Relationships
    user = relationship("User", back_populates="analytics_events")

    def __repr__(self):
        return f"<AnalyticsEvent(id={self.id}, event_type='{self.event_type}', user_id={self.user_id})>"


class VoiceAgentInteraction(Base):
    """Model for tracking voice agent interactions"""
    __tablename__ = "voice_agent_interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    interaction_metadata = Column(JSON, nullable=False, default={})
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    is_successful = Column(Boolean, default=True, nullable=False)
    session_id = Column(String(50), nullable=True, index=True)
    
    # Relationships
    user = relationship("User", back_populates="voice_interactions")
    
    def __repr__(self):
        return f"<VoiceAgentInteraction(id={self.id}, user_id={self.user_id}, session_id='{self.session_id}')>"


class UserSession(Base):
    """Model for tracking user sessions"""
    __tablename__ = "user_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), nullable=False, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    device_info = Column(JSON, nullable=False, default={})
    ip_address = Column(String(50), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="sessions")
    
    def __repr__(self):
        return f"<UserSession(id={self.id}, user_id={self.user_id}, active={self.is_active})>"
