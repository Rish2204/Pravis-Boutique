from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.repositories.voice import VoiceRepository

router = APIRouter()

@router.delete("/clear-history")
async def clear_voice_history(
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user),
):
    """
    Clear a user's voice interaction history
    """
    try:
        # Require authentication for this endpoint
        if current_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required"
            )
            
        # Delete voice history from database
        voice_repo = VoiceRepository(db)
        deleted_count = await voice_repo.delete_voice_interactions(user_id=current_user.id)
        
        return {
            "success": True,
            "message": f"Voice history cleared successfully. {deleted_count} records deleted.",
            "user_id": current_user.id,
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error clearing voice history: {str(e)}"
        )
