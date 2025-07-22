"""
Repository for User model to handle database operations
"""
from typing import List, Optional, Dict, Any

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class UserRepository:
    """Repository for User model"""
    
    @staticmethod
    def get(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_multi(db: Session, *, skip: int = 0, limit: int = 100) -> List[User]:
        """Get multiple users with pagination"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def create(db: Session, *, obj_in: UserCreate) -> User:
        """Create a new user"""
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_active=obj_in.is_active,
            is_superuser=obj_in.is_superuser,
            preferences={}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @staticmethod
    def update(db: Session, *, db_obj: User, obj_in: UserUpdate) -> User:
        """Update a user"""
        update_data = obj_in.dict(exclude_unset=True)
        
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
            
        for field in update_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
                
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    @staticmethod
    def delete(db: Session, *, user_id: int) -> Optional[User]:
        """Delete a user"""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
    
    @staticmethod
    def authenticate(db: Session, *, email: str, password: str) -> Optional[User]:
        """Authenticate a user"""
        user = UserRepository.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    @staticmethod
    def is_active(user: User) -> bool:
        """Check if user is active"""
        return user.is_active
    
    @staticmethod
    def is_superuser(user: User) -> bool:
        """Check if user is superuser"""
        return user.is_superuser
    
    @staticmethod
    def update_preferences(db: Session, *, user_id: int, preferences: Dict[str, Any]) -> User:
        """Update user preferences"""
        user = UserRepository.get(db, user_id=user_id)
        if not user:
            return None
            
        # Merge existing preferences with new ones
        user_prefs = user.preferences or {}
        user_prefs.update(preferences)
        user.preferences = user_prefs
        
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
