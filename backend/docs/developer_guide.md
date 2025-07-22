# Pravis Boutique API Developer Guide

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [Architecture](#architecture)
- [Authentication](#authentication)
- [Middleware](#middleware)
- [Monitoring](#monitoring)
- [Caching](#caching)
- [Database](#database)
- [Azure Storage Integration](#azure-storage-integration)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Overview

The Pravis Boutique API is a FastAPI-based backend service that provides:
- User authentication and management
- Voice API integration
- Analytics and history tracking
- Health monitoring endpoints

The system is designed to be scalable, secure, and maintainable, with comprehensive logging and monitoring capabilities.

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Redis (for caching)
- Azure Account (for production environment)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd pravis-boutique-backend
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the development server:
```bash
uvicorn main:app --reload
```

### Environment Variables

Create a `.env` file in the project root with the following variables:

```dotenv
# Application
APP_NAME="Pravis Boutique API"
ENVIRONMENT=development  # development, staging, production

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/pravis_collection_raw_data
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pravis_collection_raw_data
DB_USER=postgres
DB_PASSWORD=yourpassword

# Authentication
SECRET_KEY=your-secret-key  # Generate a secure random key for production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
FRONTEND_URL=http://localhost:3000

# Redis Cache
REDIS_URL=redis://localhost:6379

# Azure Storage
AZURE_STORAGE_CONNECTION_STRING=your-connection-string
AZURE_STORAGE_CONTAINER_NAME=backups

# Azure Monitoring (for production)
AZURE_APP_INSIGHTS_KEY=your-app-insights-key
AZURE_LOG_ANALYTICS_WORKSPACE_ID=your-workspace-id
AZURE_LOG_ANALYTICS_SHARED_KEY=your-shared-key
```

## API Documentation

When the server is running, API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Architecture

The application follows a modular architecture with the following components:

```
app/
├── api/                # API route definitions
│   └── api_v1/         # Version 1 API endpoints
│       └── endpoints/  # Individual API endpoints
├── core/               # Core application components
├── db/                 # Database setup and session management
├── middleware/         # Custom middleware
├── models/             # Database models (SQLAlchemy)
├── repositories/       # Data access layer
├── schemas/            # Pydantic schemas for request/response validation
└── services/           # Business logic services
```

## Authentication

The API uses JWT-based authentication with OAuth2 password flow:

1. Users authenticate via `/api/v1/auth/login`
2. The server issues a JWT token with a configurable expiry
3. Clients include the token in the `Authorization` header for subsequent requests

Protected endpoints require a valid token, which is verified using the `Depends(get_current_user)` dependency.

## Middleware

The application includes several middleware components:

- **RequestLoggingMiddleware**: Logs request and response details
- **AzureMonitoringMiddleware**: Sends telemetry data to Azure
- **RateLimiter**: Prevents API abuse with configurable rate limits
- **CacheMiddleware**: Caches responses for improved performance
- **CORSMiddleware**: Handles Cross-Origin Resource Sharing

## Monitoring

Monitoring is implemented through Azure Application Insights and Log Analytics:

- All API requests are logged with unique request IDs
- Exceptions are captured and sent to Azure
- Voice API requests are tracked with performance metrics
- Application startup and system events are monitored

The monitoring components are automatically enabled in non-development environments.

## Caching

API responses are cached using Redis:

- GET responses are cached with a configurable TTL (default: 5 minutes)
- Cache keys are generated based on the request path, query parameters, and body
- Large responses (>100KB) are not cached
- Cache hits/misses are indicated in the `X-Cache` response header
- Individual endpoints can be decorated with the `@cached` decorator

## Database

The application uses PostgreSQL with SQLAlchemy ORM:

- Models are defined in the `app/models` directory
- Database sessions are managed through the `app/db/session.py` module
- Migrations are handled using Alembic

## Azure Storage Integration

Azure Blob Storage is used for:

- Storing voice recordings and exports
- Backing up important data
- File sharing between services

Configuration is managed through the `app/services/azure_storage.py` module.

## Testing

Run tests with pytest:

```bash
pytest
```

The testing framework includes:
- API endpoint tests
- Authentication tests
- Repository/service unit tests
- Integration tests

## Deployment

See the [DEPLOYMENT.md](../DEPLOYMENT.md) file for detailed deployment instructions.

## Contributing

1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Commit your changes (`git commit -m 'Add some feature'`)
3. Push to the branch (`git push origin feature/your-feature`)
4. Create a new Pull Request
