"""
AI interaction models for tracking and analyzing user-AI agent interactions.
These models are used for logging and future model training.
"""

from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Dict, Any, Optional

from app.db.session import Base
from app.models.user import User


class AIInteraction(Base):
    """
    Model for tracking AI agent interactions.
    This data is valuable for improving AI performance and training future models.
    """
    __tablename__ = "ai_interactions"

    id = Column(Integer, primary_key=True, index=True)
    
    # User information (if authenticated)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="ai_interactions")
    
    # Session tracking
    session_id = Column(String(64), index=True, nullable=False)
    client_ip = Column(String(45), nullable=True)  # IPv6 can be up to 45 chars
    user_agent = Column(String(512), nullable=True)
    
    # Interaction details
    interaction_type = Column(String(50), nullable=False)  # e.g., 'transcription', 'tts', 'chat'
    request_text = Column(Text, nullable=True)  # User input text/query
    response_text = Column(Text, nullable=True)  # AI response text
    
    # Performance metrics
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    duration_ms = Column(Float, nullable=True)
    tokens_input = Column(Integer, nullable=True)
    tokens_output = Column(Integer, nullable=True)
    
    # Context and additional data
    context = Column(JSON, nullable=True)  # Additional context about the interaction
    interaction_metadata = Column(JSON, nullable=True)  # Any other metadata (e.g., model parameters)
    
    # Outcome and feedback
    success = Column(Boolean, default=True, nullable=False)
    error_type = Column(String(100), nullable=True)
    error_message = Column(Text, nullable=True)
    
    # Feedback and quality metrics
    user_rating = Column(Integer, nullable=True)  # e.g., 1-5 rating
    user_feedback = Column(Text, nullable=True)  # Free-form user feedback
    
    # Model and version information
    model_name = Column(String(100), nullable=True)
    model_version = Column(String(50), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<AIInteraction id={self.id} type={self.interaction_type} user_id={self.user_id}>"


class AIFeedback(Base):
    """
    Model for storing detailed user feedback about AI interactions.
    This data helps improve AI quality and user experience.
    """
    __tablename__ = "ai_feedback"

    id = Column(Integer, primary_key=True, index=True)
    
    # Associated interaction
    interaction_id = Column(Integer, ForeignKey("ai_interactions.id"), nullable=False)
    interaction = relationship("AIInteraction", backref="feedback_entries")
    
    # User information
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User")
    
    # Feedback details
    rating = Column(Integer, nullable=False)  # Numerical rating (e.g., 1-5)
    comment = Column(Text, nullable=True)  # Textual feedback
    
    # Categorization and analysis
    category = Column(String(100), nullable=True)  # e.g., 'accuracy', 'relevance', 'tone'
    sentiment_score = Column(Float, nullable=True)  # Analyzed sentiment (-1.0 to 1.0)
    tags = Column(JSON, nullable=True)  # Array of tags/topics from the feedback
    
    # Admin fields
    reviewed = Column(Boolean, default=False, nullable=False)
    reviewer_notes = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<AIFeedback id={self.id} interaction_id={self.interaction_id} rating={self.rating}>"


# Update User model relationship (will be reflected in app/models/user.py)
if not hasattr(User, 'ai_interactions'):
    User.ai_interactions = relationship("AIInteraction", back_populates="user")
