"""
Repository for voice interaction models
"""
from datetime import datetime
from typing import List, Optional, Dict, Any

from sqlalchemy import func, desc, cast, Date
from sqlalchemy.orm import Session

from app.models.analytics import VoiceInteraction
from app.schemas.analytics import VoiceInteractionMetrics


class VoiceRepository:
    """Repository for voice interaction data"""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def create_voice_interaction(
        self, 
        *, 
        user_id: Optional[int], 
        command: str, 
        response: str, 
        context: str, 
        timestamp: datetime,
        audio_data: Optional[Dict[str, Any]] = None,
        is_successful: bool = True
    ) -> VoiceInteraction:
        """Create a new voice interaction record"""
        # Prepare metadata with context and complete voice data
        metadata = {
            'context': context,
            'voice_data': audio_data or {},
            'timestamp_iso': timestamp.isoformat(),
            'user_id': user_id
        }
        
        db_obj = VoiceInteraction(
            user_id=user_id,
            query=command,
            response=response,
            interaction_metadata=metadata,
            is_successful=is_successful,
            timestamp=timestamp
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    async def delete_voice_interactions(self, *, user_id: int) -> int:
        """Delete all voice interactions for a user"""
        result = self.db.query(VoiceInteraction).filter(
            VoiceInteraction.user_id == user_id
        ).delete()
        self.db.commit()
        return result
    
    async def get_user_interactions(
        self, 
        *, 
        user_id: int,
        limit: int = 100, 
        offset: int = 0
    ) -> List[VoiceInteraction]:
        """Get all voice interactions for a user"""
        return self.db.query(VoiceInteraction).filter(
            VoiceInteraction.user_id == user_id
        ).order_by(desc(VoiceInteraction.timestamp)).offset(offset).limit(limit).all()
    
    async def get_interactions_in_range(
        self,
        *,
        start_date: datetime,
        end_date: datetime,
        user_id: Optional[int] = None,
        limit: int = 1000
    ) -> List[VoiceInteraction]:
        """Get voice interactions within a date range"""
        query = self.db.query(VoiceInteraction).filter(
            VoiceInteraction.timestamp >= start_date,
            VoiceInteraction.timestamp <= end_date
        )
        
        if user_id is not None:
            query = query.filter(VoiceInteraction.user_id == user_id)
            
        return query.order_by(desc(VoiceInteraction.timestamp)).limit(limit).all()
    
    async def get_interaction_metrics(
        self, 
        *, 
        user_id: Optional[int] = None,
        days: int = 30
    ) -> VoiceInteractionMetrics:
        """Get metrics for voice interactions"""
        from datetime import timedelta
        
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        query = self.db.query(VoiceInteraction).filter(
            VoiceInteraction.timestamp >= start_date
        )
        
        if user_id:
            query = query.filter(VoiceInteraction.user_id == user_id)
        
        interactions = query.all()
        
        total = len(interactions)
        successful = sum(1 for i in interactions if i.is_successful)
        avg_query_length = 0
        
        if total > 0:
            avg_query_length = sum(len(i.query) for i in interactions) / total
        
        # Get interactions by day
        query = self.db.query(
            cast(VoiceInteraction.timestamp, Date).label('day'),
            func.count(VoiceInteraction.id).label('count')
        ).filter(VoiceInteraction.timestamp >= start_date)
        
        if user_id:
            query = query.filter(VoiceInteraction.user_id == user_id)
        
        by_day_result = query.group_by(cast(VoiceInteraction.timestamp, Date)).all()
        by_day = {day.strftime('%Y-%m-%d'): count for day, count in by_day_result}
        
        return VoiceInteractionMetrics(
            total_interactions=total,
            successful_interactions=successful,
            average_query_length=avg_query_length,
            interactions_by_day=by_day
        )
