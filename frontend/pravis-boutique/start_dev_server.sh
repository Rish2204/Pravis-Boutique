#!/bin/bash

# Create log file with timestamp
LOG_FILE="dev_server_$(date +%Y%m%d_%H%M%S).log"

echo "Starting development server..."
echo "Logs will be saved to: $LOG_FILE"

# Start npm dev server in background and capture output
npm run dev > "$LOG_FILE" 2>&1 &
NPM_PID=$!

echo "Server starting with PID: $NPM_PID"

# Function to cleanup
cleanup() {
    echo "Stopping server (PID: $NPM_PID)..."
    kill $NPM_PID 2>/dev/null
    wait $NPM_PID 2>/dev/null
    echo "Server stopped."
    exit
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Wait for server to start
echo "Waiting for server to start..."
sleep 5

# Monitor logs for server ready and errors
BROWSER_OPENED=false
while true; do
    if kill -0 $NPM_PID 2>/dev/null; then
        # Check if server is ready and browser hasn't been opened yet
        if grep -q "Local:" "$LOG_FILE" && [ "$BROWSER_OPENED" = false ]; then
            URL=$(grep "Local:" "$LOG_FILE" | grep -o "http://localhost:[0-9]*" | head -1)
            if [ ! -z "$URL" ]; then
                echo "Server ready! Opening browser at $URL"
                open "$URL"
                BROWSER_OPENED=true
            fi
        fi
        
        # Check for errors
        if grep -qi "error\|failed\|exception\|EADDRINUSE" "$LOG_FILE"; then
            echo "ERROR DETECTED! Stopping server..."
            echo "Check log file: $LOG_FILE"
            echo "Recent logs:"
            tail -20 "$LOG_FILE"
            cleanup
        fi
        
        sleep 2
    else
        echo "Server process ended."
        break
    fi
done

wait
