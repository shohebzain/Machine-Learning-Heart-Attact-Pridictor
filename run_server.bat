@echo off
REM Heart Attack Prediction Website - Startup Script
REM This script activates the virtual environment and starts the Flask app

echo ========================================
echo Heart Attack Prediction Website
echo ========================================
echo. 

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo [!] Error: Could not activate virtual environment
    echo [*] Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo [✓] Virtual environment activated

REM Install/update dependencies
echo.
echo [*] Checking dependencies...
pip install -r requirements.txt --only-binary :all: > nul 2>&1

if errorlevel 1 (
    echo [!] Warning: Some dependencies may not be installed
)

echo [✓] Dependencies ready

REM Start the Flask app
echo.
echo [*] Starting Flask application...
echo [*] Server will be available at http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
