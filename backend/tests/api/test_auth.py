import pytest
from unittest import mock
from fastapi import HTTPException

from app.models.user import User
from app.core.security import create_access_token, get_password_hash

def test_login(client, db_session):
    """Test user login endpoint"""
    # Create a test user
    from app.core.security import get_password_hash
    
    # Create a test user in the database
    test_user = User(
        email="test@example.com",
        hashed_password=get_password_hash("password123"),
        full_name="Test User",
        is_active=True
    )
    db_session.add(test_user)
    db_session.commit()
    
    # Test valid login
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "password123"}
    )
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    
    # Test invalid password
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "wrongpassword"}
    )
    
    assert response.status_code == 401
    
    # Test non-existent user
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "nonexistent@example.com", "password": "password123"}
    )
    
    assert response.status_code == 401

def test_get_current_user(client, db_session):
    """Test get current user endpoint"""
    # Create a test user
    from app.core.security import get_password_hash
    
    test_user = User(
        email="test@example.com",
        hashed_password=get_password_hash("password123"),
        full_name="Test User",
        is_active=True
    )
    db_session.add(test_user)
    db_session.commit()
    
    # Generate a token for the user
    access_token = create_access_token(subject=str(test_user.id))
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # Test with valid token
    response = client.get("/api/v1/auth/me", headers=headers)
    
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert response.json()["full_name"] == "Test User"
    
    # Test with invalid token
    response = client.get(
        "/api/v1/auth/me", 
        headers={"Authorization": "Bearer invalidtoken"}
    )
    
    assert response.status_code == 401

def test_password_reset_request(client, db_session):
    """Test password reset request endpoint"""
    # Create a test user
    from app.core.security import get_password_hash
    
    test_user = User(
        email="test@example.com",
        hashed_password=get_password_hash("password123"),
        full_name="Test User",
        is_active=True
    )
    db_session.add(test_user)
    db_session.commit()
    
    # Mock the send_password_reset_email function
    with mock.patch('app.api.api_v1.endpoints.auth.send_password_reset_email') as mock_send:
        # Test with valid email
        response = client.post(
            "/api/v1/auth/password-reset-request",
            json={"email": "test@example.com"}
        )
        
        assert response.status_code == 200
        assert mock_send.called_once
        
        # Test with non-existent email
        response = client.post(
            "/api/v1/auth/password-reset-request",
            json={"email": "nonexistent@example.com"}
        )
        
        # Should still return 200 for security reasons (not revealing if email exists)
        assert response.status_code == 200
