"""
Azure Storage service for storing voice data
"""
import os
import json
import base64
import io
from datetime import datetime
from typing import List, Dict, Any, Optional

from azure.storage.blob import BlobServiceClient, ContentSettings
from azure.core.exceptions import ResourceExistsError


class AzureStorageService:
    """Service for interacting with Azure Blob Storage"""
    
    def __init__(self):
        """Initialize the Azure Storage service"""
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = os.getenv("AZURE_VOICE_CONTAINER", "voice-data")
        self.client = None
        
        if self.connection_string:
            self.client = BlobServiceClient.from_connection_string(self.connection_string)
    
    async def save_voice_data(
        self, 
        user_id: Optional[int], 
        audio_data: Dict[str, Any],
        metadata: Dict[str, Any]
    ) -> str:
        """
        Save voice data to Azure Storage
        
        Args:
            user_id: Optional user ID
            audio_data: Dictionary containing audio data (with base64 encoded audio)
            metadata: Additional metadata about the voice interaction
            
        Returns:
            URL of the saved blob
        """
        if not self.client:
            raise ValueError("Azure Storage not configured")
        
        # Create container if it doesn't exist
        try:
            container_client = self.client.create_container(
                name=self.container_name, 
                public_access="blob"
            )
        except ResourceExistsError:
            container_client = self.client.get_container_client(self.container_name)
        
        # Generate a unique blob name
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        user_part = f"user_{user_id}" if user_id else "anonymous"
        blob_name = f"{user_part}/{timestamp}_{hash(str(audio_data))}.json"
        
        # Prepare data for storage
        storage_data = {
            "audio_data": audio_data,
            "metadata": metadata,
            "stored_at": datetime.utcnow().isoformat(),
            "user_id": user_id
        }
        
        # Convert to JSON
        json_data = json.dumps(storage_data)
        
        # Upload to Azure
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(
            json_data,
            overwrite=True,
            content_settings=ContentSettings(content_type="application/json")
        )
        
        return blob_client.url
    
    async def save_audio_file(
        self, 
        user_id: Optional[int], 
        audio_base64: str,
        file_format: str = "webm",
        metadata: Dict[str, Any] = None
    ) -> str:
        """
        Save audio file to Azure Storage
        
        Args:
            user_id: Optional user ID
            audio_base64: Base64 encoded audio data
            file_format: Audio file format
            metadata: Additional metadata
            
        Returns:
            URL of the saved blob
        """
        if not self.client:
            raise ValueError("Azure Storage not configured")
        
        # Create container if it doesn't exist
        try:
            container_client = self.client.create_container(
                name=self.container_name, 
                public_access="blob"
            )
        except ResourceExistsError:
            container_client = self.client.get_container_client(self.container_name)
        
        # Generate a unique blob name
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        user_part = f"user_{user_id}" if user_id else "anonymous"
        blob_name = f"{user_part}/{timestamp}.{file_format}"
        
        # Decode base64 data
        audio_bytes = base64.b64decode(audio_base64)
        
        # Upload to Azure
        blob_client = container_client.get_blob_client(blob_name)
        
        content_type = "audio/webm"
        if file_format == "mp3":
            content_type = "audio/mpeg"
        elif file_format == "wav":
            content_type = "audio/wav"
        
        blob_client.upload_blob(
            audio_bytes,
            overwrite=True,
            content_settings=ContentSettings(content_type=content_type)
        )
        
        # Save metadata separately if provided
        if metadata:
            metadata_blob_name = f"{user_part}/{timestamp}_metadata.json"
            metadata_blob_client = container_client.get_blob_client(metadata_blob_name)
            
            metadata_json = json.dumps({
                "audio_blob": blob_name,
                "metadata": metadata,
                "stored_at": datetime.utcnow().isoformat(),
                "user_id": user_id
            })
            
            metadata_blob_client.upload_blob(
                metadata_json,
                overwrite=True,
                content_settings=ContentSettings(content_type="application/json")
            )
        
        return blob_client.url
    
    async def get_voice_data(self, blob_name: str) -> Dict[str, Any]:
        """
        Retrieve voice data from Azure Storage
        
        Args:
            blob_name: Name of the blob to retrieve
            
        Returns:
            Dictionary containing the voice data
        """
        if not self.client:
            raise ValueError("Azure Storage not configured")
        
        container_client = self.client.get_container_client(self.container_name)
        blob_client = container_client.get_blob_client(blob_name)
        
        blob_data = blob_client.download_blob()
        json_data = blob_data.readall()
        
        return json.loads(json_data)
    
    async def list_voice_data(
        self, 
        user_id: Optional[int] = None,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        List voice data blobs for a user
        
        Args:
            user_id: Optional user ID to filter by
            limit: Maximum number of blobs to return
            
        Returns:
            List of blob information dictionaries
        """
        if not self.client:
            raise ValueError("Azure Storage not configured")
        
        container_client = self.client.get_container_client(self.container_name)
        
        prefix = None
        if user_id:
            prefix = f"user_{user_id}/"
            
        blobs = []
        count = 0
        
        for blob in container_client.list_blobs(name_starts_with=prefix):
            if count >= limit:
                break
                
            if blob.name.endswith(".json"):
                blobs.append({
                    "name": blob.name,
                    "size": blob.size,
                    "created_on": blob.creation_time.isoformat(),
                    "url": f"{container_client.url}/{blob.name}"
                })
                count += 1
        
        return blobs
    
    async def delete_voice_data(self, blob_name: str) -> bool:
        """
        Delete voice data from Azure Storage
        
        Args:
            blob_name: Name of the blob to delete
            
        Returns:
            True if successfully deleted
        """
        if not self.client:
            raise ValueError("Azure Storage not configured")
        
        container_client = self.client.get_container_client(self.container_name)
        blob_client = container_client.get_blob_client(blob_name)
        
        blob_client.delete_blob()
        return True
