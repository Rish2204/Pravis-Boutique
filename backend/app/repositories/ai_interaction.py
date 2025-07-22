"""
Repository for AI interactions.
Provides methods for creating, retrieving, and analyzing AI interaction data.
"""

from typing import List, Dict, Any, Optional, Tuple, Union
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, and_, or_, Integer
import json
import logging

from app.models.ai_interaction import AIInteraction, AIFeedback
from app.schemas.ai_interaction import (
    AIInteractionCreate,
    AIInteractionUpdate,
    AIFeedbackCreate,
    AIFeedbackUpdate,
    AIFeedbackSummary,
    AIInteractionStats
)

logger = logging.getLogger(__name__)


class AIInteractionRepository:
    """Repository for managing AI interaction data."""

    @staticmethod
    async def create_interaction(
        db: Session,
        interaction: AIInteractionCreate,
        client_ip: Optional[str] = None,
        user_agent: Optional[str] = None
    ) -> AIInteraction:
        """
        Create a new AI interaction record.
        
        Args:
            db: Database session
            interaction: Interaction data to create
            client_ip: Optional client IP address
            user_agent: Optional user agent string
            
        Returns:
            The created AIInteraction object
        """
        # Create interaction object with client info if not provided
        interaction_data = interaction.dict()
        if not interaction_data.get("client_ip") and client_ip:
            interaction_data["client_ip"] = client_ip
        if not interaction_data.get("user_agent") and user_agent:
            interaction_data["user_agent"] = user_agent
            
        # JSON fields need to be properly serialized
        if interaction_data.get("context"):
            interaction_data["context"] = interaction_data["context"]
        if interaction_data.get("metadata"):
            interaction_data["interaction_metadata"] = interaction_data.pop("metadata")
            
        # Create and save the interaction
        db_interaction = AIInteraction(**interaction_data)
        db.add(db_interaction)
        db.commit()
        db.refresh(db_interaction)
        
        logger.info(
            f"Created AI interaction: id={db_interaction.id}, "
            f"type={db_interaction.interaction_type}, user_id={db_interaction.user_id}"
        )
        
        return db_interaction
    
    @staticmethod
    async def update_interaction(
        db: Session,
        interaction_id: int,
        interaction_update: AIInteractionUpdate
    ) -> Optional[AIInteraction]:
        """
        Update an existing AI interaction record.
        
        Args:
            db: Database session
            interaction_id: ID of the interaction to update
            interaction_update: Updated interaction data
            
        Returns:
            The updated AIInteraction object or None if not found
        """
        db_interaction = db.query(AIInteraction).filter(AIInteraction.id == interaction_id).first()
        if not db_interaction:
            logger.warning(f"Attempted to update non-existent AI interaction: id={interaction_id}")
            return None
            
        # Update fields
        update_data = interaction_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_interaction, key, value)
            
        # If completing the interaction, set duration
        if update_data.get("completed_at") and not update_data.get("duration_ms"):
            started = db_interaction.started_at
            completed = db_interaction.completed_at
            if started and completed:
                duration_ms = (completed - started).total_seconds() * 1000
                db_interaction.duration_ms = duration_ms
        
        db.add(db_interaction)
        db.commit()
        db.refresh(db_interaction)
        
        logger.info(f"Updated AI interaction: id={interaction_id}")
        
        return db_interaction
    
    @staticmethod
    async def get_interaction(db: Session, interaction_id: int) -> Optional[AIInteraction]:
        """
        Get an AI interaction by ID.
        
        Args:
            db: Database session
            interaction_id: ID of the interaction to retrieve
            
        Returns:
            The AIInteraction object or None if not found
        """
        return db.query(AIInteraction).filter(AIInteraction.id == interaction_id).first()
    
    @staticmethod
    async def get_user_interactions(
        db: Session,
        user_id: int,
        skip: int = 0,
        limit: int = 100,
        interaction_type: Optional[str] = None
    ) -> List[AIInteraction]:
        """
        Get AI interactions for a specific user.
        
        Args:
            db: Database session
            user_id: User ID to filter by
            skip: Number of records to skip
            limit: Maximum number of records to return
            interaction_type: Optional interaction type to filter by
            
        Returns:
            List of AIInteraction objects
        """
        query = db.query(AIInteraction).filter(AIInteraction.user_id == user_id)
        
        if interaction_type:
            query = query.filter(AIInteraction.interaction_type == interaction_type)
            
        return query.order_by(desc(AIInteraction.created_at)).offset(skip).limit(limit).all()
    
    @staticmethod
    async def get_session_interactions(
        db: Session,
        session_id: str,
        skip: int = 0,
        limit: int = 100
    ) -> List[AIInteraction]:
        """
        Get AI interactions for a specific session.
        
        Args:
            db: Database session
            session_id: Session ID to filter by
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of AIInteraction objects
        """
        return db.query(AIInteraction).filter(
            AIInteraction.session_id == session_id
        ).order_by(
            AIInteraction.created_at
        ).offset(skip).limit(limit).all()
    
    @staticmethod
    async def create_feedback(
        db: Session,
        feedback: AIFeedbackCreate
    ) -> AIFeedback:
        """
        Create a new AI feedback record.
        
        Args:
            db: Database session
            feedback: Feedback data to create
            
        Returns:
            The created AIFeedback object
        """
        # Create the feedback object
        db_feedback = AIFeedback(**feedback.dict())
        db.add(db_feedback)
        db.commit()
        db.refresh(db_feedback)
        
        # Also update the rating on the interaction
        interaction = db.query(AIInteraction).filter(
            AIInteraction.id == feedback.interaction_id
        ).first()
        
        if interaction:
            interaction.user_rating = feedback.rating
            interaction.user_feedback = feedback.comment
            db.add(interaction)
            db.commit()
        
        logger.info(
            f"Created AI feedback: id={db_feedback.id}, "
            f"interaction_id={db_feedback.interaction_id}, rating={db_feedback.rating}"
        )
        
        return db_feedback
    
    @staticmethod
    async def update_feedback(
        db: Session,
        feedback_id: int,
        feedback_update: AIFeedbackUpdate
    ) -> Optional[AIFeedback]:
        """
        Update an existing AI feedback record.
        
        Args:
            db: Database session
            feedback_id: ID of the feedback to update
            feedback_update: Updated feedback data
            
        Returns:
            The updated AIFeedback object or None if not found
        """
        db_feedback = db.query(AIFeedback).filter(AIFeedback.id == feedback_id).first()
        if not db_feedback:
            logger.warning(f"Attempted to update non-existent AI feedback: id={feedback_id}")
            return None
            
        # Update fields
        update_data = feedback_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_feedback, key, value)
        
        db.add(db_feedback)
        db.commit()
        db.refresh(db_feedback)
        
        # If rating was updated, also update it on the interaction
        if update_data.get("rating") is not None:
            interaction = db.query(AIInteraction).filter(
                AIInteraction.id == db_feedback.interaction_id
            ).first()
            
            if interaction:
                interaction.user_rating = db_feedback.rating
                if update_data.get("comment") is not None:
                    interaction.user_feedback = db_feedback.comment
                db.add(interaction)
                db.commit()
        
        logger.info(f"Updated AI feedback: id={feedback_id}")
        
        return db_feedback
    
    @staticmethod
    async def get_feedback_summary(
        db: Session,
        days: int = 30,
        interaction_type: Optional[str] = None
    ) -> AIFeedbackSummary:
        """
        Get a summary of AI feedback for a specified time period.
        
        Args:
            db: Database session
            days: Number of days to include in the summary
            interaction_type: Optional interaction type to filter by
            
        Returns:
            AIFeedbackSummary object with aggregated statistics
        """
        # Calculate the date range
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Base query filters
        filters = [AIFeedback.created_at.between(start_date, end_date)]
        
        # Add interaction type filter if specified
        if interaction_type:
            filters.append(
                AIFeedback.interaction_id.in_(
                    db.query(AIInteraction.id).filter(
                        AIInteraction.interaction_type == interaction_type
                    )
                )
            )
        
        # Get the total feedback count
        total_feedback = db.query(func.count(AIFeedback.id)).filter(*filters).scalar() or 0
        
        # Get average rating
        average_rating = db.query(
            func.avg(AIFeedback.rating)
        ).filter(*filters).scalar() or 0.0
        
        # Get rating distribution
        rating_counts = db.query(
            AIFeedback.rating, func.count(AIFeedback.id)
        ).filter(*filters).group_by(AIFeedback.rating).all()
        
        rating_distribution = {rating: count for rating, count in rating_counts}
        
        # Fill in missing ratings
        for i in range(1, 6):
            if i not in rating_distribution:
                rating_distribution[i] = 0
        
        # Get sentiment distribution
        sentiment_counts = db.query(
            func.case(
                (AIFeedback.sentiment_score > 0.3, "positive"),
                (AIFeedback.sentiment_score < -0.3, "negative"),
                else_="neutral"
            ).label("sentiment"),
            func.count(AIFeedback.id)
        ).filter(
            *filters,
            AIFeedback.sentiment_score.isnot(None)
        ).group_by("sentiment").all()
        
        sentiment_distribution = {sentiment: count for sentiment, count in sentiment_counts}
        
        # Get common tags
        # This is more complex as tags are stored in a JSON array
        # Simplified implementation:
        common_tags = []
        
        # Get recent comments
        recent_comments = db.query(AIFeedback).filter(
            *filters,
            AIFeedback.comment.isnot(None),
            func.length(AIFeedback.comment) > 0
        ).order_by(
            desc(AIFeedback.created_at)
        ).limit(10).all()
        
        recent_comments_data = []
        for comment in recent_comments:
            interaction = db.query(AIInteraction).filter(
                AIInteraction.id == comment.interaction_id
            ).first()
            
            comment_data = {
                "id": comment.id,
                "rating": comment.rating,
                "comment": comment.comment,
                "created_at": comment.created_at,
                "interaction_type": interaction.interaction_type if interaction else None
            }
            recent_comments_data.append(comment_data)
        
        return AIFeedbackSummary(
            total_feedback=total_feedback,
            average_rating=round(average_rating, 2),
            rating_distribution=rating_distribution,
            sentiment_distribution=sentiment_distribution,
            common_tags=common_tags,
            recent_comments=recent_comments_data
        )
    
    @staticmethod
    async def get_interaction_stats(
        db: Session,
        days: int = 30,
        interaction_type: Optional[str] = None
    ) -> AIInteractionStats:
        """
        Get statistics about AI interactions for a specified time period.
        
        Args:
            db: Database session
            days: Number of days to include in the statistics
            interaction_type: Optional interaction type to filter by
            
        Returns:
            AIInteractionStats object with aggregated statistics
        """
        # Calculate the date range
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Base query filters
        filters = [AIInteraction.created_at.between(start_date, end_date)]
        
        # Add interaction type filter if specified
        if interaction_type:
            filters.append(AIInteraction.interaction_type == interaction_type)
        
        # Get total interactions
        total_interactions = db.query(
            func.count(AIInteraction.id)
        ).filter(*filters).scalar() or 0
        
        # Get successful and failed interactions
        successful_interactions = db.query(
            func.count(AIInteraction.id)
        ).filter(*filters, AIInteraction.success == True).scalar() or 0
        
        failed_interactions = total_interactions - successful_interactions
        
        # Get average duration
        average_duration = db.query(
            func.avg(AIInteraction.duration_ms)
        ).filter(*filters, AIInteraction.duration_ms.isnot(None)).scalar() or 0.0
        
        # Get interaction types distribution
        type_counts = db.query(
            AIInteraction.interaction_type, func.count(AIInteraction.id)
        ).filter(*filters).group_by(AIInteraction.interaction_type).all()
        
        interaction_types = {str(interaction_type): count for interaction_type, count in type_counts}
        
        # Get average tokens
        avg_input_tokens = db.query(
            func.avg(AIInteraction.tokens_input)
        ).filter(*filters, AIInteraction.tokens_input.isnot(None)).scalar() or 0.0
        
        avg_output_tokens = db.query(
            func.avg(AIInteraction.tokens_output)
        ).filter(*filters, AIInteraction.tokens_output.isnot(None)).scalar() or 0.0
        
        average_tokens = {
            "input": round(avg_input_tokens, 2),
            "output": round(avg_output_tokens, 2),
            "total": round(avg_input_tokens + avg_output_tokens, 2)
        }
        
        # Get success rate by model
        model_stats = db.query(
            AIInteraction.model_name,
            func.count(AIInteraction.id).label("total"),
            func.sum(func.cast(AIInteraction.success, Integer)).label("successful")
        ).filter(
            *filters,
            AIInteraction.model_name.isnot(None)
        ).group_by(AIInteraction.model_name).all()
        
        success_rate_by_model = {}
        for model_name, total, successful in model_stats:
            success_rate = (successful / total) if total > 0 else 0
            success_rate_by_model[model_name] = round(success_rate * 100, 2)
        
        return AIInteractionStats(
            total_interactions=total_interactions,
            successful_interactions=successful_interactions,
            failed_interactions=failed_interactions,
            average_duration_ms=round(average_duration, 2),
            interaction_types=interaction_types,
            average_tokens=average_tokens,
            success_rate_by_model=success_rate_by_model
        )


# Create a singleton instance
ai_interaction_repository = AIInteractionRepository()
