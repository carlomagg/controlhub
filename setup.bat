@echo off
echo ============================================================
echo ControlHub Live - Initial Setup
echo ============================================================
echo.

REM Activate virtual environment
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Run migrations
echo.
echo Creating database...
python manage.py makemigrations accounts
python manage.py makemigrations devices
python manage.py makemigrations messaging
python manage.py makemigrations
python manage.py migrate

REM Create superuser
echo.
echo ============================================================
echo Creating superuser account
echo ============================================================
echo Please enter your admin credentials:
echo.
python manage.py createsuperuser

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Run: start_server.bat
echo 2. Open browser: http://localhost:8000
echo 3. Login with your admin credentials
echo 4. Go to Users and update your role to 'super_admin'
echo 5. Create a device and configure the client agent
echo.
pause
