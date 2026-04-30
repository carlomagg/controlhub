#!/bin/bash

echo "============================================================"
echo "ControlHub Live - Starting Server"
echo "============================================================"
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "WARNING: Virtual environment not found!"
    echo "Please create one: python -m venv venv"
    exit 1
fi

# Run migrations
echo ""
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start server
echo ""
echo "Starting ControlHub Live server..."
echo "Server will be available at: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""
daphne -b 0.0.0.0 -p 8000 controlhub.asgi:application
