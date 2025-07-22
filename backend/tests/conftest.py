import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.session import Base
from app.core.config import settings
from main import app
from app.db.session import get_db

# Import all models to ensure they are registered with the Base metadata
from app.models.user import User
from app.models.analytics import AnalyticsEvent, VoiceInteraction, UserSession

# Create a test database using SQLite in-memory database
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def db_engine():
    # Create the test database and tables
    Base.metadata.create_all(bind=engine)
    yield engine
    # Drop the test database after the tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(db_engine):
    # Create a new session for each test
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    # Use the session in tests
    yield session
    
    # Rollback the transaction and close the session after the test
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    # Override the get_db dependency to use the test database
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    # Replace the dependency
    app.dependency_overrides[get_db] = override_get_db
    
    # Create a test client using the FastAPI app
    with TestClient(app) as test_client:
        yield test_client
    
    # Clear the dependency override after the test
    app.dependency_overrides.clear()
