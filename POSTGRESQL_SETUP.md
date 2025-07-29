# PostgreSQL Integration Guide
## Pravis-Boutique Development Environment

---

## **System Verification Status ✅**

### **PostgreSQL Installation**
- **Version**: PostgreSQL 14.18 (Homebrew)
- **Service Status**: Active and running
- **CLI Access**: `psql` command functional
- **Service Management**: `brew services start/stop postgresql@14`

### **Database Configuration**
- **Database Name**: `pravis_collection_raw_data`
- **User Role**: `postgres`
- **Password**: `pravis_dba`
- **Connection**: Validated and operational

---

## **Environment Configuration**

### **Complete .env File**
```bash
# Application Settings
APP_NAME=Pravis Boutique API
DEBUG=True
ENVIRONMENT=development

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
FRONTEND_URL=http://localhost:3000

# Database Configuration
DATABASE_URL=postgresql://postgres:pravis_dba@localhost:5432/pravis_collection_raw_data
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pravis_collection_raw_data
DB_USER=postgres
DB_PASSWORD=pravis_dba

# Security Settings
SECRET_KEY=8fc595e71a2c9b1b1d61c8f07afb3cc03bb1e29a2c62e0e8bfe3693fae6fbc7c
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
```

---

## **Development Workflow Commands**

### **Virtual Environment Management**
```bash
# Activate environment
cd /Users/rish/Developer/Pravis-Boutique/backend
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

### **Database Operations**
```bash
# Check PostgreSQL service status
brew services list | grep postgresql

# Start PostgreSQL service
brew services start postgresql@14

# Connect to database
psql -U postgres -d pravis_collection_raw_data

# List databases
psql -l

# Create new database (if needed)
createdb -O postgres [database_name]
```

### **Connection Validation**
```bash
# Test FastAPI database connection
python -c "
from app.core.config import settings
from sqlalchemy import create_engine
try:
    engine = create_engine(settings.sqlalchemy_database_uri)
    connection = engine.connect()
    print('✅ PostgreSQL connection successful')
    connection.close()
except Exception as e:
    print(f'❌ Connection failed: {e}')
"
```

---

## **Schema Management**

### **Alembic Migration Commands**
```bash
# Check current migration status
alembic current

# View migration history
alembic history

# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback to previous migration
alembic downgrade -1
```

### **Database Schema Initialization**
```bash
# First-time setup
alembic revision --autogenerate -m "Initial database schema"
alembic upgrade head
```

---

## **FastAPI Service Management**

### **Development Server**
```bash
# Start FastAPI development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Access API documentation
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### **VS Code Ports Integration**
- **Port 8000** auto-detected when FastAPI runs
- **Local access**: Direct localhost testing
- **Port forwarding**: Enable for cross-device testing
- **Network sharing**: Access from mobile devices on same network

---

## **Dependencies Architecture**

### **Core Database Stack**
```txt
# Database Dependencies (requirements.txt)
sqlalchemy>=2.0.0,<3.0.0          # Modern ORM framework
psycopg2-binary>=2.9.6,<3.0.0     # PostgreSQL adapter
alembic>=1.11.0,<1.12.0           # Migration management
```

### **Integration Components**
- **FastAPI**: Async web framework with PostgreSQL support
- **SQLAlchemy 2.0**: Modern ORM with async capabilities
- **Pydantic**: Data validation and settings management
- **Alembic**: Database migration and version control

---

## **Troubleshooting Guide**

### **Common Issues & Solutions**

**Connection Failed - Role Does Not Exist**
```bash
# Create PostgreSQL user
createuser --createdb --pwprompt postgres

# Verify user creation
psql -U postgres -c "\du"
```

**Virtual Environment Corruption**
```bash
# Clean rebuild
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Port Already in Use**
```bash
# Find process using port 8000
lsof -i :8000

# Kill process (if needed)
kill -9 [PID]
```

**Database Connection Timeout**
```bash
# Check PostgreSQL service
brew services restart postgresql@14

# Verify port accessibility
telnet localhost 5432
```

### **Environment Validation Checklist**
- [ ] PostgreSQL service running
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip list | grep psycopg2`)
- [ ] .env file configured
- [ ] Database connection validated
- [ ] Migration status checked (`alembic current`)

---

## **Security Considerations**

### **Development vs Production**
- **Current setup**: Development credentials
- **Production requirements**: 
  - Environment variable injection
  - Secure password management
  - Azure Key Vault integration
  - Connection pooling optimization

### **Credential Management**
- **Local development**: `.env` file (gitignored)
- **Azure deployment**: Application settings
- **Team sharing**: `.env.example` template
- **Secret rotation**: Regular password updates

---

## **Strategic Development Pathway**

### **Current Status**: ✅ Database Infrastructure Complete
- PostgreSQL service operational
- FastAPI integration validated
- Environment configuration established
- Migration framework initialized

### **Next Development Phases**
1. **Schema Deployment**: Initialize core database tables
2. **API Service Validation**: Confirm endpoint accessibility
3. **Frontend Integration**: Connect Nuxt.js to FastAPI backend
4. **Authentication Implementation**: JWT user management
5. **Azure Deployment**: Production environment setup

### **Architecture Overview**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Nuxt.js PWA   │────│   FastAPI API    │────│  PostgreSQL DB  │
│   (Frontend)    │    │   (Backend)      │    │   (Database)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │                        │                        │
        │                        │                        │
    Port 3000              Port 8000               Port 5432
```

---

## **Quick Reference Commands**

### **Daily Development Workflow**
```bash
# Start development session
cd /Users/rish/Developer/Pravis-Boutique/backend
source .venv/bin/activate

# Start services
brew services start postgresql@14
uvicorn main:app --reload

# Access APIs
open http://localhost:8000/docs
```

### **Emergency Reset**
```bash
# Full environment reset
deactivate
rm -rf .venv
brew services restart postgresql@14
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

**Documentation Status**: ✅ PostgreSQL integration complete and validated  
**Last Updated**: Database connectivity established  
**Next Milestone**: Schema deployment and FastAPI service initialization
