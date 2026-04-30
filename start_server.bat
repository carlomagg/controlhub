@echo off
echo ============================================================
echo ControlHub Live - Starting Server
echo ============================================================
echo.

REM Activate virtual environment
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo WARNING: Virtual environment not found!
    echo Please create one: python -m venv venv
    pause
    exit /b 1
)

REM Run migrations
echo.
echo Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Start server
echo.
echo Starting ControlHub Live server...
echo Server will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
daphne -b 0.0.0.0 -p 8000 controlhub.asgi:application
