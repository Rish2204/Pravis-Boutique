from app.schemas.base import (
    HTTPError,
    ValidationError,
    HTTPValidationError,
    ResponseBase,
    PaginatedResponseBase,
)

from app.schemas.health import (
    HealthResponse,
    DatabaseHealthResponse,
)

from app.schemas.auth import (
    User,
    UserCreate,
    UserUpdate,
    UserInDB,
    LoginRequest,
    TokenResponse,
)

from app.schemas.analytics import (
    AnalyticsEventBase,
    AnalyticsEventCreate, 
    AnalyticsEventInDB,
    VoiceInteractionBase,
    VoiceInteractionCreate, 
    VoiceInteractionInDB,
    UserSessionBase,
    UserSessionCreate,
    UserSessionUpdate,
    UserSessionInDB,
    AnalyticsReport,
    VoiceInteractionMetrics
)
