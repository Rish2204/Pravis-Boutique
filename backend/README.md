# FastAPI Backend

A simple FastAPI backend application with a "Hello, World!" endpoint.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- PostgreSQL (for database functionality)

## Project Structure

```
backend/
├── main.py              # Main FastAPI application file
├── database.py          # Database configuration and connection
├── db_utils.py          # Database utility functions
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .env                 # Your local environment variables (not in git)
├── .gitignore          # Files to ignore in git
├── venv/               # Virtual environment (created during setup)
└── README.md           # This file
```

## Quick Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd Automation-Playground/backend
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up PostgreSQL Database**:
   - Create a `.env` file in the backend directory:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` with your PostgreSQL credentials:
     ```
     DATABASE_URL=postgresql://your_username:your_password@localhost:5432/marketing_analytics
     ```
   - Test your database connection:
     ```bash
     python db_utils.py
     ```

## Running the Application

### Option 1: Using uvicorn directly (Recommended)
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

### Option 2: With auto-reload (for development)
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Option 3: Running in the background
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 &
```

## Testing the API

Once the server is running, you can test it:

### Using curl:
```bash
curl http://127.0.0.1:8000/
```

Expected response:
```json
{"Hello": "World"}
```

### Using a web browser:
Navigate to `http://127.0.0.1:8000/`

### API Documentation:
FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Common Issues and Solutions

### ModuleNotFoundError: No module named 'backend'
If you encounter this error, make sure you're running the command from the `backend` directory:
```bash
cd backend
uvicorn main:app --host 127.0.0.1 --port 8000
```

### Port already in use
If port 8000 is already in use, you can specify a different port:
```bash
uvicorn main:app --host 127.0.0.1 --port 8001
```

### Virtual environment not activated
Always ensure your virtual environment is activated before running the application. You should see `(venv)` in your terminal prompt.

## Stopping the Server

- If running in the foreground: Press `Ctrl+C`
- If running in the background: Use `kill %1` or find the process ID with `ps aux | grep uvicorn` and use `kill <PID>`

## Development Tips

1. **Using Warp Terminal**: This project works seamlessly with Warp terminal. You can use Warp's AI features to help with development.

2. **API Testing Tools**: 
   - **Insomnia**: A modern, clean API client with great UX
   - **Postman**: Feature-rich API platform with collaboration features
   - **curl**: Command-line tool for quick testing

3. **Adding new endpoints**: Edit `main.py` to add new routes:
   ```python
   @app.get("/new-endpoint")
   def new_endpoint():
       return {"message": "New endpoint"}
   ```

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **Uvicorn**: Lightning-fast ASGI server implementation

## Next Steps

- Add more endpoints to `main.py`
- Create data models using Pydantic
- Add database integration (e.g., MemSQL)
- Implement authentication
- Add tests

## Support

If you encounter any issues, please check:
1. Python version: `python --version` (should be 3.9+)
2. Virtual environment is activated
3. All dependencies are installed: `pip list`
4. You're in the correct directory: `pwd` (should end with `/backend`)
