@echo off
echo ========================================
echo   CodeMaster - Setup Script
echo ========================================
echo.

echo [1/4] Creating virtual environment...
python -m venv venv
echo Done!

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate
echo Done!

echo.
echo [3/4] Installing dependencies...
pip install -r requirements.txt
echo Done!

echo.
echo [4/4] Running database migrations...
python manage.py migrate
echo Done!

echo.
echo ========================================
echo   Setup Complete!
echo   Run: python manage.py runserver
echo ========================================
pause
