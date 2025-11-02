@echo off
REM Quick start script for Windows
echo Starting FastAPI backend...
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause

