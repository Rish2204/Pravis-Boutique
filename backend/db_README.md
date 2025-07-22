# Database Integration for Pravis Boutique

This document describes the comprehensive database integration setup for the Pravis Boutique application.

## Overview

The database integration for Pravis Boutique uses:
- **SQLAlchemy ORM** for data modeling and abstract database operations
- **Alembic** for versioned schema migrations
- **PostgreSQL** as the database backend
- **Pydantic** for data validation and serialization

## Database Models

The following database models have been implemented:

### User Model
- Core user entity for authentication and user management
- Stores user credentials, profile information, and preferences

### Analytics Models
- **AnalyticsEvent**: General-purpose event tracking
- **VoiceInteraction**: Voice agent interactions with users
- **UserSession**: User session tracking

## Database Utilities

The `db_utils.py` file provides comprehensive utilities for:
- Generic CRUD operations via the `CRUDBase` class
- Query utilities for pagination, filtering, and sorting
- Analytics-specific functions for recording events and interactions
- Raw SQL execution capability

## Migrations

Database migrations are managed using Alembic:

1. Initial schema migration (001_initial_database_schema.py)
   - Creates the base tables for users, analytics events, voice interactions, and user sessions

## Repository Pattern

The application implements the repository pattern to abstract database operations:

- **UserRepository**: User management operations
- **AnalyticsRepository**: General analytics event operations
- **VoiceInteractionRepository**: Voice interaction tracking
- **UserSessionRepository**: User session management

## How to Run Migrations

To initialize the database and apply migrations:

```bash
# Initialize the database (if it doesn't exist)
python -m backend.db_utils

# Run migrations
cd backend
alembic upgrade head
```

To create a new migration:

```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
```

## Schema Validation

Pydantic models are used for data validation and serialization:

- Input validation (Create/Update schemas)
- Response serialization (InDB schemas)
- Analytics reporting models

## Best Practices

1. Always use the repository pattern for database operations
2. Create Alembic migrations for all schema changes
3. Use SQLAlchemy ORM for database queries rather than raw SQL
4. Validate all input data using Pydantic models
5. Handle database errors gracefully in service layers

## Analytics Features

The analytics models support:

1. **Event Tracking**: Record general user and system events
2. **Voice Interaction Analysis**: Track and analyze voice agent interactions
3. **Session Monitoring**: Track user sessions and engagement metrics
4. **Reporting**: Generate analytics reports and metrics
