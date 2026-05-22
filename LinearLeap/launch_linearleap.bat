@echo off
cd /d "%~dp0"
echo ==========================================
echo   Starting LinearLeap Application
echo ==========================================
echo.

REM Start the API server in a new window
echo Starting API Server on port 5000...
start "LinearLeap API Server" cmd /k "python api.py"

REM Wait a moment for API server to start
timeout /t 2 /nobreak >nul

REM Start the frontend HTTP server in a new window
echo Starting Frontend Server on port 8000...
start "LinearLeap Frontend Server" cmd /k "cd frontend && python -m http.server 8000"

REM Wait a moment for frontend server to start
timeout /t 2 /nobreak >nul

REM Open the browser
echo Opening browser...
start http://localhost:8000/index.html

echo.
echo ==========================================
echo   LinearLeap is now running!
echo ==========================================
echo   Frontend: http://localhost:8000
echo   API:      http://localhost:5000
echo.
echo   Close both server windows to stop.
echo ==========================================
pause
