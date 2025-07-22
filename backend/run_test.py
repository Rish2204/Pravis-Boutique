import os
import sys
import uvicorn

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app

if __name__ == "__main__":
    # Run the app
    uvicorn.run(app, host="127.0.0.1", port=8000)
