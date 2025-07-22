from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, status, BackgroundTasks, Request
from fastapi.responses import StreamingResponse
from typing import Dict, Any, Optional, List, Tuple
import io
import os
import tempfile
import uuid
import json
import time
import hashlib
import base64
import whisper
import aiofiles
from openai import OpenAI
from datetime import datetime, timedelta

from app.api.deps import get_db, get_current_user
from app.models.analytics import VoiceInteraction
from app.models.user import User
from app.repositories.voice import VoiceRepository
from sqlalchemy.orm import Session
from app.middleware.cache import cached

# Import Azure Blob Storage client for caching audio files
from azure.storage.blob import BlobServiceClient, ContentSettings
from azure.core.exceptions import ResourceExistsError

router = APIRouter()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load Whisper model - use a smaller model for faster processing
whisper_model_size = os.getenv("WHISPER_MODEL_SIZE", "base")
whisper_model = None  # Lazy-loaded when needed

# Define voice model
tts_voice = os.getenv("TTS_VOICE_MODEL", "nova")  # Options: alloy, echo, fable, onyx, nova, shimmer

# Azure Blob Storage for caching
blob_service_client = None
blob_container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "voice-cache")

# In-memory cache for frequently used TTS responses (limited size)
tts_cache = {}

# Maximum size of the in-memory TTS cache
MAX_TTS_CACHE_ENTRIES = 100

# Time-to-live for cached TTS responses (in seconds)
TTS_CACHE_TTL = 86400  # 24 hours

# Create timestamp for cache management
TTS_CACHE_TIMESTAMPS = {}

# Audio transcription cache (in-memory, temporary)
transcription_cache = {}
MAX_TRANSCRIPTION_CACHE_ENTRIES = 50
TRANSCRIPTION_CACHE_TTL = 3600  # 1 hour
TRANSCRIPTION_CACHE_TIMESTAMPS = {}

# OpenAI response cache (for identical prompts)
openai_response_cache = {}
MAX_OPENAI_CACHE_ENTRIES = 100
OPENAI_CACHE_TTL = 3600  # 1 hour
OPENAI_CACHE_TIMESTAMPS = {}

# Azure Blob Storage initialization
def get_blob_service_client():
    global blob_service_client
    if blob_service_client is None:
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        if connect_str:
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            # Ensure container exists
            try:
                container_client = blob_service_client.create_container(blob_container_name)
            except ResourceExistsError:
                # Container already exists, just get a reference to it
                container_client = blob_service_client.get_container_client(blob_container_name)
    return blob_service_client

def get_whisper_model():
    """Lazy-load the Whisper model to save memory until needed"""
    global whisper_model
    if whisper_model is None:
        print(f"Loading Whisper model: {whisper_model_size}")
        start_time = time.time()
        whisper_model = whisper.load_model(whisper_model_size)
        print(f"Whisper model loaded in {time.time() - start_time:.2f} seconds")
    return whisper_model


def clean_cache(cache: Dict, timestamps: Dict, max_entries: int, ttl: int):
    """Clean expired or excess cache entries"""
    now = datetime.utcnow()
    
    # Remove expired entries
    expired_keys = [k for k, t in timestamps.items() if now - t > timedelta(seconds=ttl)]
    for key in expired_keys:
        if key in cache:
            del cache[key]
        if key in timestamps:
            del timestamps[key]
    
    # If still too many entries, remove oldest ones
    if len(cache) > max_entries:
        # Sort keys by timestamp
        sorted_keys = sorted(timestamps.keys(), key=lambda k: timestamps[k])
        # Remove oldest entries until we're under the limit
        for key in sorted_keys[:len(cache) - max_entries]:
            if key in cache:
                del cache[key]
            if key in timestamps:
                del timestamps[key]


def generate_hash(content: bytes) -> str:
    """Generate a hash from content for caching"""
    return hashlib.md5(content).hexdigest()


def generate_text_hash(text: str, voice: str = "default") -> str:
    """Generate a hash from text and voice for TTS caching"""
    return hashlib.md5(f"{text}:{voice}".encode()).hexdigest()


async def cache_audio_to_blob(audio_content: bytes, blob_name: str):
    """Cache audio content to Azure Blob Storage"""
    try:
        blob_client = get_blob_service_client().get_blob_client(
            container=blob_container_name, 
            blob=blob_name
        )
        
        # Upload audio with appropriate content type
        content_settings = ContentSettings(content_type="audio/mpeg")
        blob_client.upload_blob(
            audio_content, 
            overwrite=True,
            content_settings=content_settings
        )
        
        return True
    except Exception as e:
        print(f"Error caching audio to blob storage: {str(e)}")
        return False


async def get_audio_from_blob(blob_name: str) -> Optional[bytes]:
    """Retrieve cached audio from Azure Blob Storage"""
    try:
        blob_client = get_blob_service_client().get_blob_client(
            container=blob_container_name, 
            blob=blob_name
        )
        
        # Check if blob exists
        if blob_client.exists():
            # Download the blob
            download_stream = blob_client.download_blob()
            return download_stream.readall()
        
        return None
    except Exception as e:
        print(f"Error retrieving audio from blob storage: {str(e)}")
        return None


async def store_voice_interaction(
    db: Session, 
    user_id: Optional[int], 
    command: str, 
    response: str, 
    context: Dict[str, Any],
    audio_data: Optional[Dict[str, Any]] = None
):
    """Store voice interaction for analytics"""
    try:
        voice_repo = VoiceRepository(db)
        await voice_repo.create_voice_interaction(
            user_id=user_id,
            command=command,
            response=response,
            context=json.dumps(context),
            timestamp=datetime.utcnow(),
            audio_data=audio_data
        )
    except Exception as e:
        # Log the error but don't fail the request
        print(f"Error storing voice interaction: {str(e)}")


@router.post("/transcribe")
async def transcribe_audio(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user),
    audio_file: UploadFile = File(...),
    save_audio: bool = False,
):
    """
    Transcribe audio using Whisper model
    """
    try:
        start_time = time.time()
        
        # Read the audio content
        content = await audio_file.read()
        
        # Generate hash for caching
        audio_hash = generate_hash(content)
        
        # Check in-memory cache first
        if audio_hash in transcription_cache:
            print(f"Transcription cache hit for {audio_hash}")
            # Update timestamp
            TRANSCRIPTION_CACHE_TIMESTAMPS[audio_hash] = datetime.utcnow()
            return transcription_cache[audio_hash]
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".webm")
        temp_file_path = temp_file.name
        
        # Write to temp file
        async with aiofiles.open(temp_file_path, 'wb') as out_file:
            await out_file.write(content)
        
        # Get Whisper model and transcribe
        model = get_whisper_model()
        result = model.transcribe(temp_file_path)
        
        # Create response object
        response_data = {
            "text": result["text"],
            "language": result.get("language", "en"),
            "segments": result.get("segments", [])
        }
        
        # Cache the result in memory
        transcription_cache[audio_hash] = response_data
        TRANSCRIPTION_CACHE_TIMESTAMPS[audio_hash] = datetime.utcnow()
        
        # Clean up cache if needed
        background_tasks.add_task(
            clean_cache, 
            transcription_cache, 
            TRANSCRIPTION_CACHE_TIMESTAMPS, 
            MAX_TRANSCRIPTION_CACHE_ENTRIES, 
            TRANSCRIPTION_CACHE_TTL
        )
        
        print(f"Transcription completed in {time.time() - start_time:.2f} seconds")
        
        # Save audio data as base64 if requested
        audio_data = None
        if save_audio:
            try:
                import base64
                with open(temp_file_path, 'rb') as audio_file:
                    audio_bytes = audio_file.read()
                    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
                    
                audio_data = {
                    'audio_base64': audio_base64,
                    'format': 'webm',
                    'transcription': result["text"],
                    'language': result.get("language", "en"),
                    'timestamp': datetime.utcnow().isoformat()
                }
                
                # Store the interaction with audio data
                user_id = current_user.id if current_user else None
                background_tasks.add_task(
                    store_voice_interaction,
                    db,
                    user_id,
                    result["text"],
                    "Audio transcription",
                    {},
                    audio_data
                )
            except Exception as e:
                print(f"Error saving audio data: {str(e)}")
        
        # Clean up temp file in background
        background_tasks.add_task(os.unlink, temp_file_path)
        
        # Return transcription
        return {
            "text": result["text"],
            "language": result.get("language", "en"),
            "segments": result.get("segments", [])
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing audio: {str(e)}"
        )


@router.post("/process-command")
async def process_voice_command(
    command: Dict[str, Any],
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user),
):
    """
    Process a voice command using AI
    """
    try:
        start_time = time.time()
        
        text = command.get("text", "")
        context = command.get("context", {})
        
        if not text:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No text provided"
            )
        
        # Create cache key based on the input text
        cache_key = generate_hash(text.encode())
        
        # Check cache for this command
        if cache_key in openai_response_cache:
            print(f"OpenAI cache hit for {cache_key}")
            # Update timestamp
            OPENAI_CACHE_TIMESTAMPS[cache_key] = datetime.utcnow()
            parsed_response = openai_response_cache[cache_key]
        else:
            # Process with OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",  # or "gpt-3.5-turbo" for lower cost
                messages=[
                    {
                        "role": "system", 
                        "content": """
                        You are a helpful boutique voice assistant. Answer questions about:
                        - Products (clothing, accessories)
                        - Store policies (returns, exchanges, shipping)
                        - Size guides and recommendations
                        - Availability and pricing
                        
                        If the user is asking to navigate somewhere or perform an action, respond 
                        with a friendly confirmation and include an action object in your response.
                        
                        Examples of actions:
                        - {"type": "navigate", "path": "/products"}
                        - {"type": "addToCart", "productId": "123"}
                        - {"type": "search", "query": "red dress"}
                        - {"type": "checkout"}
                        
                        Your response should be conversational, helpful, and concise.
                        """
                    },
                    {"role": "user", "content": text}
                ],
                response_format={"type": "json_object"}
            )
            
            # Parse the response
            content = response.choices[0].message.content
            parsed_response = json.loads(content)
            
            # Cache the result
            openai_response_cache[cache_key] = parsed_response
            OPENAI_CACHE_TIMESTAMPS[cache_key] = datetime.utcnow()
            
            # Clean up cache if needed
            background_tasks.add_task(
                clean_cache, 
                openai_response_cache, 
                OPENAI_CACHE_TIMESTAMPS, 
                MAX_OPENAI_CACHE_ENTRIES, 
                OPENAI_CACHE_TTL
            )
            
            print(f"OpenAI request completed in {time.time() - start_time:.2f} seconds")
        
        # Store interaction for analytics
        user_id = current_user.id if current_user else None
        background_tasks.add_task(
            store_voice_interaction,
            db,
            user_id,
            text,
            parsed_response.get("text", ""),
            context
        )
        
        return parsed_response
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing command: {str(e)}"
        )


@router.post("/text-to-speech")
async def generate_speech(
    text_data: Dict[str, Any],
    background_tasks: BackgroundTasks,
):
    """
    Generate speech from text using OpenAI TTS
    """
    try:
        start_time = time.time()
        
        text = text_data.get("text", "")
        voice = text_data.get("voice", tts_voice)
        
        if not text:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No text provided"
            )
        
        # Create a hash for caching
        text_hash = generate_text_hash(text, voice)
        blob_name = f"tts/{text_hash}.mp3"
        
        # Check in-memory cache first (fastest)
        if text_hash in tts_cache:
            print(f"TTS in-memory cache hit for {text_hash}")
            # Update timestamp
            TTS_CACHE_TIMESTAMPS[text_hash] = datetime.utcnow()
            return StreamingResponse(
                io.BytesIO(tts_cache[text_hash]),
                media_type="audio/mpeg",
                headers={"Content-Disposition": f"attachment; filename=speech-{text_hash}.mp3", "X-Cache": "HIT"}
            )
        
        # Check Azure Blob Storage cache (slower but persistent)
        if get_blob_service_client():
            cached_audio = await get_audio_from_blob(blob_name)
            if cached_audio:
                print(f"TTS blob cache hit for {text_hash}")
                # Update in-memory cache too
                tts_cache[text_hash] = cached_audio
                TTS_CACHE_TIMESTAMPS[text_hash] = datetime.utcnow()
                return StreamingResponse(
                    io.BytesIO(cached_audio),
                    media_type="audio/mpeg",
                    headers={"Content-Disposition": f"attachment; filename=speech-{text_hash}.mp3", "X-Cache": "HIT"}
                )
        
        # No cache hit, generate new speech
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        
        # Cache the result in memory
        tts_cache[text_hash] = response.content
        TTS_CACHE_TIMESTAMPS[text_hash] = datetime.utcnow()
        
        # Clean up cache if needed
        background_tasks.add_task(
            clean_cache, 
            tts_cache, 
            TTS_CACHE_TIMESTAMPS, 
            MAX_TTS_CACHE_ENTRIES, 
            TTS_CACHE_TTL
        )
        
        # Cache to Azure Blob Storage in the background
        if get_blob_service_client():
            background_tasks.add_task(cache_audio_to_blob, response.content, blob_name)
        
        print(f"TTS generation completed in {time.time() - start_time:.2f} seconds")
        
        # Return audio stream
        return StreamingResponse(
            io.BytesIO(response.content),
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": f"attachment; filename=speech-{text_hash}.mp3",
                "X-Cache": "MISS"
            }
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating speech: {str(e)}"
        )


@router.get("/voices")
@cached(ttl=3600)  # Cache for 1 hour
async def list_available_voices():
    """
    List available TTS voices
    """
    voices = [
        {"id": "alloy", "name": "Alloy", "gender": "neutral"},
        {"id": "echo", "name": "Echo", "gender": "male"},
        {"id": "fable", "name": "Fable", "gender": "female"},
        {"id": "onyx", "name": "Onyx", "gender": "male"},
        {"id": "nova", "name": "Nova", "gender": "female"},
        {"id": "shimmer", "name": "Shimmer", "gender": "female"}
    ]
    
    return {"voices": voices}


@router.get("/health")
@cached(ttl=60)  # Cache for 1 minute
async def check_voice_api_health():
    """
    Check health of voice API and its dependencies
    """
    openai_status = "ok"
    whisper_status = "ok"
    azure_blob_status = "ok"
    
    try:
        # Simple check to see if OpenAI API is accessible
        client.models.list(limit=1)
    except Exception:
        openai_status = "error"
    
    try:
        # Just check if we can access the whisper model
        get_whisper_model()
    except Exception:
        whisper_status = "error"
    
    try:
        # Check Azure Blob Storage
        if get_blob_service_client() is None:
            azure_blob_status = "not_configured"
    except Exception:
        azure_blob_status = "error"
    
    # Report on cache sizes
    cache_info = {
        "tts_cache_size": len(tts_cache),
        "transcription_cache_size": len(transcription_cache),
        "openai_cache_size": len(openai_response_cache)
    }
    
    return {
        "status": "ok" if openai_status == "ok" and whisper_status == "ok" else "error",
        "openai": openai_status,
        "whisper": whisper_status,
        "azure_blob": azure_blob_status,
        "caches": cache_info,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/cache/stats")
@cached(ttl=60)  # Cache for 1 minute
async def get_cache_stats():
    """
    Get statistics about the caching system
    """
    # Calculate TTL expirations
    now = datetime.utcnow()
    
    tts_expirations = [
        (key, (timestamps + timedelta(seconds=TTS_CACHE_TTL) - now).total_seconds())
        for key, timestamps in TTS_CACHE_TIMESTAMPS.items()
    ]
    
    transcription_expirations = [
        (key, (timestamps + timedelta(seconds=TRANSCRIPTION_CACHE_TTL) - now).total_seconds())
        for key, timestamps in TRANSCRIPTION_CACHE_TIMESTAMPS.items()
    ]
    
    openai_expirations = [
        (key, (timestamps + timedelta(seconds=OPENAI_CACHE_TTL) - now).total_seconds())
        for key, timestamps in OPENAI_CACHE_TIMESTAMPS.items()
    ]
    
    # Get blob storage stats if available
    blob_stats = {}
    if get_blob_service_client():
        try:
            container_client = get_blob_service_client().get_container_client(blob_container_name)
            blobs = list(container_client.list_blobs())
            blob_stats = {
                "total_blobs": len(blobs),
                "total_size_bytes": sum(b.size for b in blobs),
                "tts_blobs": len([b for b in blobs if b.name.startswith("tts/")])
            }
        except Exception as e:
            blob_stats = {"error": str(e)}
    
    return {
        "caches": {
            "tts": {
                "in_memory_entries": len(tts_cache),
                "max_entries": MAX_TTS_CACHE_ENTRIES,
                "ttl_seconds": TTS_CACHE_TTL
            },
            "transcription": {
                "in_memory_entries": len(transcription_cache),
                "max_entries": MAX_TRANSCRIPTION_CACHE_ENTRIES,
                "ttl_seconds": TRANSCRIPTION_CACHE_TTL
            },
            "openai": {
                "in_memory_entries": len(openai_response_cache),
                "max_entries": MAX_OPENAI_CACHE_ENTRIES,
                "ttl_seconds": OPENAI_CACHE_TTL
            }
        },
        "blob_storage": blob_stats,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.post("/cache/clear")
async def clear_cache(cache_type: Optional[str] = None):
    """
    Clear cache entries
    """
    global tts_cache, TTS_CACHE_TIMESTAMPS
    global transcription_cache, TRANSCRIPTION_CACHE_TIMESTAMPS
    global openai_response_cache, OPENAI_CACHE_TIMESTAMPS
    
    cleared = []
    
    if cache_type is None or cache_type == "tts":
        tts_cache = {}
        TTS_CACHE_TIMESTAMPS = {}
        cleared.append("tts")
    
    if cache_type is None or cache_type == "transcription":
        transcription_cache = {}
        TRANSCRIPTION_CACHE_TIMESTAMPS = {}
        cleared.append("transcription")
    
    if cache_type is None or cache_type == "openai":
        openai_response_cache = {}
        OPENAI_CACHE_TIMESTAMPS = {}
        cleared.append("openai")
    
    if cache_type is None or cache_type == "blob":
        # Clear blob storage if configured
        if get_blob_service_client():
            try:
                container_client = get_blob_service_client().get_container_client(blob_container_name)
                blobs = list(container_client.list_blobs())
                for blob in blobs:
                    blob_client = container_client.get_blob_client(blob.name)
                    blob_client.delete_blob()
                cleared.append("blob_storage")
            except Exception as e:
                return {
                    "success": False,
                    "error": f"Failed to clear blob storage: {str(e)}",
                    "cleared": cleared
                }
    
    return {
        "success": True,
        "cleared": cleared,
        "timestamp": datetime.utcnow().isoformat()
    }
