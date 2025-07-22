"""
Repository for analytics models to handle database operations
"""
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any, Tuple

from sqlalchemy import func, desc, cast, Date
from sqlalchemy.orm import Session

from app.models.analytics import AnalyticsEvent, VoiceInteraction, UserSession
from app.schemas.analytics import (
    AnalyticsEventCreate, 
    VoiceInteractionCreate,
    UserSessionCreate,
    UserSessionUpdate,
    AnalyticsReport,
    VoiceInteractionMetrics
)


class AnalyticsRepository:
    """Repository for analytics models"""
    
    @staticmethod
    def create_event(db: Session, *, obj_in: AnalyticsEventCreate) -> AnalyticsEvent:
        """Create a new analytics event"""
        db_obj = AnalyticsEvent(
            event_type=obj_in.event_type,
            user_id=obj_in.user_id,
            event_data=obj_in.event_data,
            timestamp=datetime.utcnow()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @staticmethod
    def get_events(
        db: Session, 
        *, 
        skip: int = 0, 
        limit: int = 100,
        event_type: Optional[str] = None,
        user_id: Optional[int] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[AnalyticsEvent]:
        """Get analytics events with filtering and pagination"""
        query = db.query(AnalyticsEvent)
        
        if event_type:
            query = query.filter(AnalyticsEvent.event_type == event_type)
        if user_id:
            query = query.filter(AnalyticsEvent.user_id == user_id)
        if start_date:
            query = query.filter(AnalyticsEvent.timestamp >= start_date)
        if end_date:
            query = query.filter(AnalyticsEvent.timestamp <= end_date)
        
        return query.order_by(desc(AnalyticsEvent.timestamp)).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_event_counts_by_type(
        db: Session, 
        *, 
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, int]:
        """Get event counts grouped by event_type"""
        query = db.query(
            AnalyticsEvent.event_type, 
            func.count(AnalyticsEvent.id).label('count')
        )
        
        if start_date:
            query = query.filter(AnalyticsEvent.timestamp >= start_date)
        if end_date:
            query = query.filter(AnalyticsEvent.timestamp <= end_date)
        
        result = query.group_by(AnalyticsEvent.event_type).all()
        return {event_type: count for event_type, count in result}
    
    @staticmethod
    def get_event_counts_by_day(
        db: Session, 
        *, 
        days: int = 7,
        event_type: Optional[str] = None
    ) -> Dict[str, int]:
        """Get event counts grouped by day for the last N days"""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        query = db.query(
            cast(AnalyticsEvent.timestamp, Date).label('day'),
            func.count(AnalyticsEvent.id).label('count')
        ).filter(AnalyticsEvent.timestamp >= start_date)
        
        if event_type:
            query = query.filter(AnalyticsEvent.event_type == event_type)
        
        result = query.group_by(cast(AnalyticsEvent.timestamp, Date)).all()
        return {day.strftime('%Y-%m-%d'): count for day, count in result}
    
    @staticmethod
    def get_analytics_report(
        db: Session, 
        *, 
        days: int = 30
    ) -> AnalyticsReport:
        """Generate an analytics report"""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Get total events
        total_events = db.query(func.count(AnalyticsEvent.id)).filter(
            AnalyticsEvent.timestamp >= start_date
        ).scalar() or 0
        
        # Get events by type
        events_by_type = AnalyticsRepository.get_event_counts_by_type(
            db, start_date=start_date, end_date=end_date
        )
        
        # Get events by day
        events_by_day = AnalyticsRepository.get_event_counts_by_day(
            db, days=days
        )
        
        return AnalyticsReport(
            total_events=total_events,
            events_by_type=events_by_type,
            events_by_day=events_by_day
        )


class VoiceInteractionRepository:
    """Repository for voice interaction analytics"""
    
    @staticmethod
    def create_interaction(db: Session, *, obj_in: VoiceInteractionCreate) -> VoiceInteraction:
        """Create a new voice interaction record"""
        db_obj = VoiceInteraction(
            user_id=obj_in.user_id,
            query=obj_in.query,
            response=obj_in.response,
            metadata=obj_in.metadata,
            is_successful=obj_in.is_successful,
            session_id=obj_in.session_id,
            timestamp=datetime.utcnow()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @staticmethod
    def get_interactions(
        db: Session, 
        *, 
        skip: int = 0, 
        limit: int = 100,
        user_id: Optional[int] = None,
        session_id: Optional[str] = None,
        is_successful: Optional[bool] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[VoiceInteraction]:
        """Get voice interactions with filtering and pagination"""
        query = db.query(VoiceInteraction)
        
        if user_id:
            query = query.filter(VoiceInteraction.user_id == user_id)
        if session_id:
            query = query.filter(VoiceInteraction.session_id == session_id)
        if is_successful is not None:
            query = query.filter(VoiceInteraction.is_successful == is_successful)
        if start_date:
            query = query.filter(VoiceInteraction.timestamp >= start_date)
        if end_date:
            query = query.filter(VoiceInteraction.timestamp <= end_date)
        
        return query.order_by(desc(VoiceInteraction.timestamp)).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_interaction_metrics(
        db: Session, 
        *, 
        days: int = 30,
        user_id: Optional[int] = None
    ) -> VoiceInteractionMetrics:
        """Get metrics for voice interactions"""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        query = db.query(VoiceInteraction).filter(VoiceInteraction.timestamp >= start_date)
        if user_id:
            query = query.filter(VoiceInteraction.user_id == user_id)
        
        interactions = query.all()
        
        total = len(interactions)
        successful = sum(1 for i in interactions if i.is_successful)
        avg_query_length = 0
        if total > 0:
            avg_query_length = sum(len(i.query) for i in interactions) / total
        
        # Get interactions by day
        query = db.query(
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


class UserSessionRepository:
    """Repository for user session tracking"""
    
    @staticmethod
    def create_session(db: Session, *, obj_in: UserSessionCreate) -> UserSession:
        """Create a new user session"""
        db_obj = UserSession(
            session_id=obj_in.session_id,
            user_id=obj_in.user_id,
            is_active=True,
            device_info=obj_in.device_info,
            ip_address=obj_in.ip_address,
            started_at=datetime.utcnow(),
            ended_at=None
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @staticmethod
    def end_session(db: Session, *, session_id: str, obj_in: UserSessionUpdate) -> Optional[UserSession]:
        """End a user session"""
        session = db.query(UserSession).filter(UserSession.session_id == session_id).first()
        if not session:
            return None
        
        session.ended_at = obj_in.ended_at or datetime.utcnow()
        session.is_active = False
        
        db.add(session)
        db.commit()
        db.refresh(session)
        return session
    
    @staticmethod
    def get_active_sessions(
        db: Session, 
        *, 
        user_id: Optional[int] = None
    ) -> List[UserSession]:
        """Get active user sessions"""
        query = db.query(UserSession).filter(UserSession.is_active == True)
        if user_id:
            query = query.filter(UserSession.user_id == user_id)
        return query.all()
    
    @staticmethod
    def get_session_by_id(db: Session, *, session_id: str) -> Optional[UserSession]:
        """Get a session by its ID"""
        return db.query(UserSession).filter(UserSession.session_id == session_id).first()
    
    @staticmethod
    def get_user_sessions(
        db: Session, 
        *, 
        user_id: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[UserSession]:
        """Get all sessions for a user"""
        return db.query(UserSession).filter(
            UserSession.user_id == user_id
        ).order_by(desc(UserSession.started_at)).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_session_stats(
        db: Session, 
        *, 
        days: int = 30
    ) -> Tuple[int, int, float]:
        """Get session statistics: total, active, and average duration"""
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Get all sessions in the period
        sessions = db.query(UserSession).filter(UserSession.started_at >= start_date).all()
        
        total_sessions = len(sessions)
        active_sessions = sum(1 for s in sessions if s.is_active)
        
        # Calculate average duration for completed sessions
        durations = []
        for session in sessions:
            if not session.is_active and session.ended_at:
                duration = (session.ended_at - session.started_at).total_seconds()
                durations.append(duration)
        
        avg_duration = sum(durations) / len(durations) if durations else 0
        
        return total_sessions, active_sessions, avg_duration
