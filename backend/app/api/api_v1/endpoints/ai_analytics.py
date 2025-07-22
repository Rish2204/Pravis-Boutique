"""
API endpoints for AI interaction analytics.
Provides endpoints for logging and analyzing AI interactions.
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Header
from sqlalchemy.orm import Session
from uuid import uuid4

from app.db.session import get_db
from app.core.auth import get_current_user
from app.repositories.ai_interaction import ai_interaction_repository
from app.schemas.ai_interaction import (
    AIInteractionCreate,
    AIInteractionUpdate,
    AIInteractionResponse,
    AIFeedbackCreate,
    AIFeedbackResponse,
    AIFeedbackSummary,
    AIInteractionStats
)

router = APIRouter()


@router.post("/interactions", response_model=AIInteractionResponse)
async def create_ai_interaction(
    interaction: AIInteractionCreate,
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Log a new AI interaction.
    
    This endpoint records interactions between users and AI agents for monitoring,
    analytics, and future model training.
    """
    # Get client information
    client_ip = request.client.host
    user_agent = request.headers.get("User-Agent")
    
    # Use authenticated user ID if available
    if current_user and not interaction.user_id:
        interaction.user_id = current_user["id"]
    
    # Create the interaction
    db_interaction = await ai_interaction_repository.create_interaction(
        db=db,
        interaction=interaction,
        client_ip=client_ip,
        user_agent=user_agent
    )
    
    return db_interaction


@router.patch("/interactions/{interaction_id}", response_model=AIInteractionResponse)
async def update_ai_interaction(
    interaction_id: int,
    interaction_update: AIInteractionUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update an AI interaction with results or feedback.
    
    This endpoint is used to update an existing interaction with response data,
    completion information, or error details.
    """
    # Update the interaction
    db_interaction = await ai_interaction_repository.update_interaction(
        db=db,
        interaction_id=interaction_id,
        interaction_update=interaction_update
    )
    
    if not db_interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    
    return db_interaction


@router.get("/interactions/{interaction_id}", response_model=AIInteractionResponse)
async def get_ai_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get details of a specific AI interaction.
    
    Retrieves comprehensive information about a single AI interaction by ID.
    """
    db_interaction = await ai_interaction_repository.get_interaction(
        db=db,
        interaction_id=interaction_id
    )
    
    if not db_interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    
    # Check if user has access to this interaction
    if db_interaction.user_id and db_interaction.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this interaction")
    
    return db_interaction


@router.get("/interactions/user/{user_id}", response_model=List[AIInteractionResponse])
async def get_user_interactions(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    interaction_type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get AI interactions for a specific user.
    
    Lists all interactions for a user, with optional filtering by interaction type.
    Administrators can access any user's interactions, while regular users can only access their own.
    """
    # Check if user has access to these interactions
    if user_id != current_user["id"] and not current_user.get("is_admin", False):
        raise HTTPException(status_code=403, detail="Not authorized to access these interactions")
    
    interactions = await ai_interaction_repository.get_user_interactions(
        db=db,
        user_id=user_id,
        skip=skip,
        limit=limit,
        interaction_type=interaction_type
    )
    
    return interactions


@router.get("/interactions/session/{session_id}", response_model=List[AIInteractionResponse])
async def get_session_interactions(
    session_id: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get AI interactions for a specific session.
    
    Lists all interactions for a session, useful for tracking conversation history.
    Users can only access sessions they participated in.
    """
    interactions = await ai_interaction_repository.get_session_interactions(
        db=db,
        session_id=session_id,
        skip=skip,
        limit=limit
    )
    
    # Check if user has access to this session
    if interactions and interactions[0].user_id and interactions[0].user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this session")
    
    return interactions


@router.post("/feedback", response_model=AIFeedbackResponse)
async def create_ai_feedback(
    feedback: AIFeedbackCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Submit feedback for an AI interaction.
    
    This endpoint allows users to provide ratings and comments on AI interactions,
    which helps improve the quality of AI responses.
    """
    # Use authenticated user ID if available
    if current_user and not feedback.user_id:
        feedback.user_id = current_user["id"]
    
    # Create the feedback
    db_feedback = await ai_interaction_repository.create_feedback(
        db=db,
        feedback=feedback
    )
    
    return db_feedback


@router.get("/analytics/feedback-summary", response_model=AIFeedbackSummary)
async def get_feedback_summary(
    days: int = Query(30, ge=1, le=365),
    interaction_type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get a summary of AI feedback.
    
    This endpoint provides aggregated statistics about user feedback on AI interactions,
    including ratings distribution and sentiment analysis.
    
    Only administrators can access this endpoint.
    """
    # Check if user is an administrator
    if not current_user.get("is_admin", False):
        raise HTTPException(status_code=403, detail="Only administrators can access this endpoint")
    
    summary = await ai_interaction_repository.get_feedback_summary(
        db=db,
        days=days,
        interaction_type=interaction_type
    )
    
    return summary


@router.get("/analytics/interaction-stats", response_model=AIInteractionStats)
async def get_interaction_stats(
    days: int = Query(30, ge=1, le=365),
    interaction_type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get statistics about AI interactions.
    
    This endpoint provides aggregated statistics about AI interactions,
    including success rates, average response times, and token usage.
    
    Only administrators can access this endpoint.
    """
    # Check if user is an administrator
    if not current_user.get("is_admin", False):
        raise HTTPException(status_code=403, detail="Only administrators can access this endpoint")
    
    stats = await ai_interaction_repository.get_interaction_stats(
        db=db,
        days=days,
        interaction_type=interaction_type
    )
    
    return stats


@router.post("/client/log-event", status_code=202)
async def log_client_event(
    event: dict,
    x_api_key: Optional[str] = Header(None),
    request: Request = None,
    db: Session = Depends(get_db)
):
    """
    Log a client-side event for analytics.
    
    This endpoint allows frontend clients to log events such as page views,
    feature usage, errors, and other user interactions for analytics purposes.
    
    Authentication is done via API key to allow anonymous tracking.
    """
    # Simple API key validation - in production, use a more secure approach
    if not x_api_key or x_api_key != "valid-tracking-api-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # Add client information to event
    if request:
        event["client_ip"] = request.client.host
        event["user_agent"] = request.headers.get("User-Agent")
    
    # Generate session ID if not provided
    if "session_id" not in event:
        event["session_id"] = str(uuid4())
    
    # In a real implementation, we would store this event in a suitable storage system
    # For this example, we'll just acknowledge receipt
    
    return {"status": "accepted"}
