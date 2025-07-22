"""
Endpoints for exporting voice data to Azure Blob Storage
"""
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

from app.api.deps import get_db, get_current_user, get_current_active_superuser
from app.models.user import User
from app.repositories.voice import VoiceRepository
from app.services.azure_storage import AzureStorageService

router = APIRouter()
azure_service = AzureStorageService()

@router.post("/export/azure")
async def export_voice_data_to_azure(
    background_tasks: BackgroundTasks,
    days: int = 7,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_superuser),
):
    """
    Export voice data to Azure Blob Storage (admin/superuser only)
    """
    try:
        # Check if Azure Storage is configured
        if not azure_service.client:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Azure Storage not configured"
            )
        
        # Get voice data from repository
        voice_repo = VoiceRepository(db)
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        # Query for voice interactions in date range
        interactions = await voice_repo.get_interactions_in_range(
            start_date=start_date,
            end_date=end_date
        )
        
        if not interactions:
            return {
                "success": True,
                "message": "No voice data found for export",
                "count": 0
            }
        
        # Process in the background
        background_tasks.add_task(
            export_interactions_to_azure,
            interactions
        )
        
        return {
            "success": True,
            "message": f"Exporting {len(interactions)} voice interactions to Azure Storage",
            "count": len(interactions)
        }
    
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error exporting voice data: {str(e)}"
        )


@router.get("/export/status")
async def get_export_status(
    current_user: User = Depends(get_current_active_superuser),
):
    """
    Get status of voice data exports (admin/superuser only)
    """
    # This is a placeholder for a real implementation that would track export jobs
    return {
        "status": "available",
        "message": "Export functionality is available",
        "azure_storage_configured": azure_service.client is not None
    }


@router.get("/azure/list")
async def list_azure_voice_data(
    user_id: Optional[int] = None,
    limit: int = 100,
    current_user: User = Depends(get_current_active_superuser),
):
    """
    List voice data stored in Azure (admin/superuser only)
    """
    try:
        # Check if Azure Storage is configured
        if not azure_service.client:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Azure Storage not configured"
            )
        
        # List voice data from Azure
        blobs = await azure_service.list_voice_data(
            user_id=user_id,
            limit=limit
        )
        
        return {
            "count": len(blobs),
            "items": blobs
        }
    
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error listing voice data: {str(e)}"
        )


async def export_interactions_to_azure(interactions: List[Any]):
    """
    Background task to export voice interactions to Azure
    """
    for interaction in interactions:
        try:
            # Check if there's audio data in the metadata
            metadata = interaction.interaction_metadata
            audio_data = metadata.get("voice_data", {}) if metadata else {}
            
            if audio_data and "audio_base64" in audio_data:
                # If we have audio data, save it separately
                await azure_service.save_audio_file(
                    user_id=interaction.user_id,
                    audio_base64=audio_data["audio_base64"],
                    file_format=audio_data.get("format", "webm"),
                    metadata={
                        "interaction_id": interaction.id,
                        "query": interaction.query,
                        "response": interaction.response,
                        "timestamp": interaction.timestamp.isoformat(),
                        "is_successful": interaction.is_successful
                    }
                )
            else:
                # Otherwise save the entire interaction data
                export_data = {
                    "id": interaction.id,
                    "query": interaction.query,
                    "response": interaction.response,
                    "timestamp": interaction.timestamp.isoformat(),
                    "is_successful": interaction.is_successful,
                    "session_id": interaction.session_id,
                    "metadata": metadata
                }
                
                await azure_service.save_voice_data(
                    user_id=interaction.user_id,
                    audio_data={},  # Empty since we don't have audio data
                    metadata=export_data
                )
        except Exception as e:
            # Log error but continue with other interactions
            print(f"Error exporting interaction {interaction.id}: {str(e)}")
            continue
