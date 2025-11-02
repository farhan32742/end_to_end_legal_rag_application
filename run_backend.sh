#!/bin/bash
# Quick start script for Linux/Mac
echo "Starting FastAPI backend..."
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

