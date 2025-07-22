import pytest
import json
import io
from unittest import mock
from fastapi import UploadFile, BackgroundTasks

from app.api.api_v1.endpoints.voice_api import (
    transcribe_audio, 
    process_voice_command,
    generate_speech,
    list_available_voices,
    check_voice_api_health
)

# Test for voice health endpoint
def test_voice_api_health(client):
    """Test the voice API health endpoint"""
    with mock.patch('app.api.api_v1.endpoints.voice_api.client.models.list') as mock_list:
        mock_list.return_value = {"data": [{"id": "test-model"}]}
        
        response = client.get("/api/v1/voice/health")
        
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
        assert "timestamp" in response.json()

# Test for listing available voices
def test_list_available_voices(client):
    """Test the endpoint that lists available TTS voices"""
    response = client.get("/api/v1/voice/voices")
    
    assert response.status_code == 200
    assert "voices" in response.json()
    assert len(response.json()["voices"]) > 0
    
    # Verify the structure of the voice objects
    for voice in response.json()["voices"]:
        assert "id" in voice
        assert "name" in voice
        assert "gender" in voice

# Test for processing voice commands
def test_process_voice_command(client):
    """Test the process voice command endpoint"""
    # Mock the OpenAI response
    mock_response = mock.MagicMock()
    mock_response.choices = [
        mock.MagicMock(
            message=mock.MagicMock(
                content='{"text": "This is a test response", "action": null}'
            )
        )
    ]
    
    with mock.patch('app.api.api_v1.endpoints.voice_api.client.chat.completions.create') as mock_create:
        mock_create.return_value = mock_response
        
        # Test with valid command
        response = client.post(
            "/api/v1/voice/process-command",
            json={"text": "What products do you have?", "context": {}}
        )
        
        assert response.status_code == 200
        assert "text" in response.json()
        assert response.json()["text"] == "This is a test response"

# Test for transcribing audio
@mock.patch('app.api.api_v1.endpoints.voice_api.get_whisper_model')
@mock.patch('aiofiles.open')
@mock.patch('tempfile.NamedTemporaryFile')
def test_transcribe_audio(mock_temp_file, mock_aiofiles, mock_get_whisper_model, client):
    """Test the audio transcription endpoint"""
    # Setup mocks
    mock_temp = mock.MagicMock()
    mock_temp.name = "/tmp/test.webm"
    mock_temp_file.return_value = mock_temp
    
    mock_file = mock.MagicMock()
    mock_aiofiles.return_value.__aenter__.return_value = mock_file
    
    mock_model = mock.MagicMock()
    mock_model.transcribe.return_value = {
        "text": "This is a test transcription",
        "language": "en",
        "segments": []
    }
    mock_get_whisper_model.return_value = mock_model
    
    # Create test file
    test_file = io.BytesIO(b"test audio content")
    
    # Test with file upload
    response = client.post(
        "/api/v1/voice/transcribe",
        files={"audio_file": ("test.webm", test_file, "audio/webm")}
    )
    
    assert response.status_code == 200
    assert "text" in response.json()
    assert response.json()["text"] == "This is a test transcription"
    assert response.json()["language"] == "en"

# Test for text-to-speech generation
def test_generate_speech(client):
    """Test the text-to-speech endpoint"""
    # Mock the OpenAI TTS response
    mock_response = mock.MagicMock()
    mock_response.content = b"fake audio data"
    
    with mock.patch('app.api.api_v1.endpoints.voice_api.client.audio.speech.create') as mock_create:
        mock_create.return_value = mock_response
        
        # Test with valid text
        response = client.post(
            "/api/v1/voice/text-to-speech",
            json={"text": "This is a test message", "voice": "nova"}
        )
        
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "audio/mpeg"
        assert "attachment; filename=speech-" in response.headers["Content-Disposition"]
        assert response.content == b"fake audio data"
