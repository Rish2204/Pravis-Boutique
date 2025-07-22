from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.core.config import settings
from app.schemas.health import HealthResponse, DatabaseHealthResponse

router = APIRouter()

@router.get("/", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def health_check() -> HealthResponse:
    """
    Basic health check endpoint to verify API is running.
    """
    return HealthResponse(
        status="ok",
        version="1.0.0",
        api="Pravis Boutique API",
        environment=settings.ENVIRONMENT,
    )

@router.get("/db", response_model=DatabaseHealthResponse)
def database_health_check(db: Session = Depends(get_db_session)) -> DatabaseHealthResponse:
    """
    Check database connectivity.
    """
    try:
        # Simple query to check database connectivity
        db.execute("SELECT 1")
        return DatabaseHealthResponse(status="ok", database="connected")
    except Exception as e:
        return DatabaseHealthResponse(
            status="error",
            database="disconnected",
            detail=str(e)
        )
