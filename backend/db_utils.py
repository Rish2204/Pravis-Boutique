#!/usr/bin/env python3
"""
Database utility functions for database operations using SQLAlchemy ORM
"""
import os
import sys
from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Callable

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import func, desc, asc, and_, or_, not_, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.expression import select, delete, update

from app.db.session import SessionLocal, Base

# Define a type variable for models
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Base class for CRUD operations"""

    def __init__(self, model: Type[ModelType]):
        """Initialize with SQLAlchemy model"""
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """Get a single record by ID"""
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """Get multiple records with pagination"""
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def get_by_attribute(
        self, db: Session, *, attr_name: str, attr_value: Any
    ) -> List[ModelType]:
        """Get records by a specific attribute"""
        return db.query(self.model).filter(
            getattr(self.model, attr_name) == attr_value
        ).all()
    
    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """Create a new record"""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(
        self, db: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """Update an existing record"""
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def remove(self, db: Session, *, id: int) -> ModelType:
        """Remove a record"""
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
    
    def count(self, db: Session) -> int:
        """Count total records"""
        return db.query(self.model).count()


def get_db_session():
    """Get a new database session"""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


def paginate_query(query: Query, page: int = 1, page_size: int = 20) -> Query:
    """Apply pagination to a query"""
    return query.offset((page - 1) * page_size).limit(page_size)


def filter_by_date_range(query: Query, model: Type[ModelType], 
                        date_field: str, start_date: datetime = None, 
                        end_date: datetime = None) -> Query:
    """Filter a query by date range"""
    if start_date:
        query = query.filter(getattr(model, date_field) >= start_date)
    if end_date:
        query = query.filter(getattr(model, date_field) <= end_date)
    return query


def search_by_field(query: Query, model: Type[ModelType], 
                   field: str, search_term: str) -> Query:
    """Search records with a case-insensitive LIKE query"""
    if search_term:
        return query.filter(getattr(model, field).ilike(f"%{search_term}%"))
    return query


def sort_query(query: Query, model: Type[ModelType], 
              sort_field: str, descending: bool = False) -> Query:
    """Sort a query by the specified field"""
    if hasattr(model, sort_field):
        order_func = desc if descending else asc
        return query.order_by(order_func(getattr(model, sort_field)))
    return query


def execute_bulk_insert(db: Session, objects: List[Any]) -> None:
    """Execute bulk insert of objects"""
    db.bulk_save_objects(objects)
    db.commit()


def record_analytics_event(db: Session, event_type: str, 
                         user_id: Optional[int], data: Dict[str, Any]) -> Any:
    """Record an analytics event
    
    This function assumes there's an AnalyticsEvent model defined.
    """
    from app.models.analytics import AnalyticsEvent
    
    event = AnalyticsEvent(
        event_type=event_type,
        user_id=user_id,
        event_data=data,
        timestamp=datetime.utcnow()
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def record_voice_interaction(db: Session, user_id: Optional[int], 
                           query: str, response: str, 
                           metadata: Dict[str, Any] = None) -> Any:
    """Record a voice agent interaction
    
    This function assumes there's a VoiceInteraction model defined.
    """
    from app.models.analytics import VoiceInteraction
    
    interaction = VoiceInteraction(
        user_id=user_id,
        query=query,
        response=response,
        metadata=metadata or {},
        timestamp=datetime.utcnow()
    )
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


def execute_raw_sql(db: Session, sql_query: str, params: Dict[str, Any] = None) -> List[Dict]:
    """Execute raw SQL query and return results as dictionaries"""
    result = db.execute(text(sql_query), params or {})
    column_names = result.keys()
    return [dict(zip(column_names, row)) for row in result.fetchall()]


if __name__ == "__main__":
    # Example usage when script is run directly
    with get_db_session() as db:
        print(f"Connected to database")
        # Example: print total users
        # from app.models.user import User
        # print(f"Total users: {db.query(User).count()}")
