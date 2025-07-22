# Pravis Boutique Project Structure

This document outlines the recommended project structure for the Pravis Boutique application, covering both the FastAPI backend and Nuxt.js frontend.

## Overall Project Structure

```
pravis-boutique/
├── backend/               # FastAPI backend application
├── frontend/              # Nuxt.js frontend application
├── scripts/               # Utility scripts for development and deployment
├── .gitignore             # Git ignore file
├── README.md              # Project overview
└── PROJECT_STRUCTURE.md   # This file
```

## Backend Structure (FastAPI)

The backend follows a modular structure with a clear separation of concerns:

```
backend/
├── alembic/               # Database migration scripts
├── app/                   # Application package
│   ├── api/               # API endpoints
│   │   ├── api_v1/        # API version 1
│   │   │   ├── endpoints/ # API route handlers
│   │   │   └── api.py     # API router aggregation
│   ├── core/              # Core functionality
│   │   ├── config.py      # Configuration settings
│   │   └── security.py    # Security utilities
│   ├── db/                # Database
│   │   ├── base.py        # Base class for models
│   │   └── session.py     # Database session management
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas for request/response
│   └── services/          # Business logic services
├── tests/                 # Test directory
│   ├── api/               # API tests
│   ├── services/          # Service tests
│   └── conftest.py        # Test fixtures
├── .env                   # Environment variables (not in git)
├── .env.example           # Example environment variables
├── alembic.ini            # Alembic configuration
├── main.py                # Application entry point
├── DEPLOYMENT.md          # Deployment documentation
└── requirements.txt       # Python dependencies
```

### Key Backend Components

1. **API Layer (`app/api/`)**: 
   - Handles HTTP requests and responses
   - Organizes endpoints by resource type
   - Implements input validation

2. **Core (`app/core/`)**: 
   - Contains configuration and application-wide utilities
   - Manages environment variables and settings

3. **Database Layer (`app/db/`)**: 
   - Manages database connections
   - Provides session utilities

4. **Models (`app/models/`)**: 
   - SQLAlchemy ORM models
   - Represents database tables and relationships

5. **Schemas (`app/schemas/`)**: 
   - Pydantic models for request/response validation
   - Data transfer objects

6. **Services (`app/services/`)**: 
   - Business logic implementation
   - Decoupled from API endpoints for reusability

## Frontend Structure (Nuxt.js)

The frontend follows the Nuxt.js recommended structure with additional organization for larger applications:

```
frontend/pravis-boutique/
├── assets/                # Static assets (processed by webpack)
│   ├── css/               # Global CSS styles
│   └── images/            # Images
├── components/            # Vue components
│   ├── common/            # Shared components
│   ├── layout/            # Layout-specific components
│   └── pages/             # Page-specific components
├── composables/           # Vue composables (shared logic)
├── layouts/               # Layout templates
├── middleware/            # Nuxt middleware
├── pages/                 # Route pages
├── plugins/               # Vue plugins
├── public/                # Static files (served as-is)
│   ├── favicon.ico        # Favicon
│   └── icons/             # PWA icons
├── server/                # Server-side code (if using SSR)
├── store/                 # Pinia store modules
├── types/                 # TypeScript type definitions
├── utils/                 # Utility functions
├── .env                   # Environment variables (not in git)
├── .env.example           # Example environment variables
├── nuxt.config.ts         # Nuxt configuration
├── package.json           # Node.js dependencies
├── DEPLOYMENT.md          # Deployment documentation
└── tsconfig.json          # TypeScript configuration
```

### Key Frontend Components

1. **Pages (`pages/`)**: 
   - Define application routes
   - Each file corresponds to a route

2. **Components (`components/`)**: 
   - Reusable Vue components
   - Organized by purpose and scope

3. **Composables (`composables/`)**: 
   - Reusable Vue composition functions
   - Encapsulate complex reactive logic

4. **Store (`store/`)**: 
   - Pinia store for state management
   - Organized by domain/feature

5. **Layouts (`layouts/`)**: 
   - Page layout templates
   - Shared structure across pages

6. **Middleware (`middleware/`)**: 
   - Route middleware
   - Authentication, permissions, etc.

## Environment Variables

Both the backend and frontend use `.env` files for environment-specific configuration:

### Backend Environment Variables

The backend uses a single `.env` file with sections for different aspects of the application:

```
# Application Settings
APP_NAME=Pravis Boutique API
DEBUG=True
ENVIRONMENT=development

# API Settings
API_HOST=0.0.0.0
API_PORT=8000
FRONTEND_URL=http://localhost:3000

# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/dbname

# Azure Configuration
AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string
AZURE_STORAGE_CONTAINER_NAME=backups
```

### Frontend Environment Variables

The frontend uses Nuxt's environment variable system with the `NUXT_` prefix for public variables:

```
# API Configuration
NUXT_PUBLIC_API_BASE_URL=http://localhost:8000
NUXT_PUBLIC_API_VERSION=/api/v1

# Application Settings
NUXT_PUBLIC_APP_NAME=Pravis Boutique
NUXT_PUBLIC_APP_DESCRIPTION=Pravis Boutique E-commerce Platform

# Feature Flags
NUXT_PUBLIC_ENABLE_VOICE_AGENT=true
NUXT_PUBLIC_ENABLE_ANALYTICS=true
```

## Dependency Management

### Backend Dependencies

The backend uses `requirements.txt` with pinned versions for reproducible builds:

```
# API Framework
fastapi>=0.97.0,<0.98.0
pydantic>=1.10.0,<2.0.0

# Server
uvicorn>=0.22.0,<0.23.0

# Database
sqlalchemy>=2.0.0,<3.0.0
psycopg2-binary>=2.9.6,<3.0.0
alembic>=1.11.0,<1.12.0

# Environment variables
python-dotenv>=1.0.0,<2.0.0

# Azure Integration
azure-storage-blob>=12.16.0,<13.0.0
```

### Frontend Dependencies

The frontend uses `package.json` for dependency management:

```json
{
  "dependencies": {
    "@nuxtjs/tailwindcss": "^6.8.4",
    "@pinia/nuxt": "^0.5.1",
    "@vite-pwa/nuxt": "^0.4.0",
    "@vueuse/core": "^10.5.0",
    "nuxt": "^3.8.0",
    "pinia": "^2.1.7",
    "vue": "^3.3.8"
  },
  "devDependencies": {
    "@nuxt/devtools": "latest",
    "eslint": "^8.52.0",
    "postcss": "^8.4.31",
    "tailwindcss": "^3.3.5"
  }
}
```

## Version Control Strategy

1. **Branching Strategy**:
   - `main`: Production-ready code
   - `develop`: Integration branch for features
   - `feature/*`: New features
   - `bugfix/*`: Bug fixes
   - `release/*`: Release preparation

2. **Environment Branches**:
   - `staging`: For staging environment
   - `production`: For production environment

3. **PR Workflow**:
   - Features → Develop → Staging → Main
   - Hotfixes can go directly to Main with backporting to Develop

## Deployment Workflows

Detailed deployment workflows are available in the respective DEPLOYMENT.md files:

- [Backend Deployment](/backend/DEPLOYMENT.md)
- [Frontend Deployment](/frontend/pravis-boutique/DEPLOYMENT.md)

## Best Practices

### Backend Best Practices

1. **Dependency Injection**:
   - Use FastAPI's dependency injection system
   - Avoid global state

2. **Type Annotations**:
   - Use Python type hints everywhere
   - Leverage Pydantic for validation

3. **API Versioning**:
   - All APIs should be versioned
   - Breaking changes should be in new versions

4. **Testing**:
   - Unit tests for services
   - Integration tests for APIs
   - Use pytest fixtures for shared setup

5. **Error Handling**:
   - Use custom exception handlers
   - Return consistent error responses

### Frontend Best Practices

1. **Component Design**:
   - Follow the Single Responsibility Principle
   - Use props for component configuration
   - Use emits for child-to-parent communication

2. **State Management**:
   - Use Pinia for global state
   - Use local component state when appropriate
   - Define clear state mutation patterns

3. **API Calls**:
   - Centralize API call logic in composables
   - Handle loading, error, and success states

4. **TypeScript**:
   - Use TypeScript interfaces for data models
   - Define prop types and return types

5. **Performance**:
   - Lazy load routes and components
   - Use efficient rendering practices
   - Optimize images and assets

## Conclusion

This project structure is designed to be scalable, maintainable, and follow industry best practices for FastAPI and Nuxt.js applications. It provides a clear separation of concerns and makes it easy to locate and modify specific parts of the application.
