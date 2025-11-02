# ⚡ FastAPI Backend Setup Guide

## 🎯 What Changed?

We've replaced the slow Express.js + Node.js backend with a **FastAPI backend** that:
- ✅ **Much Faster** - Everything loads once at startup (models, vector store)
- ✅ **Simpler** - All Python, no need for Node.js
- ✅ **Optimized** - Models are preloaded, so responses are instant
- ✅ **Production Ready** - FastAPI is built for performance

## 📁 New Structure

```
backend/
├── main.py              ← FastAPI app (replaces server.js)
└── services/
    └── rag_service.py  ← Optimized RAG service (replaces ragService.js)
```

## 🚀 Quick Start

### Step 1: Install FastAPI Dependencies

```bash
pip install fastapi uvicorn[standard] python-multipart
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### Step 2: Start the FastAPI Backend

**Option A: Using the start script (Easiest)**
```bash
python start_backend.py
```

**Option B: Manual start**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

### Step 3: Start the React Frontend (in a new terminal)

```bash
cd frontend
npm start
```

## 🎉 Access Your App

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

## ⚡ Performance Improvements

### Before (Express.js):
- ❌ Loading models on every request (slow)
- ❌ Spawning Python process for each request
- ❌ Network overhead between Node.js and Python

### After (FastAPI):
- ✅ Models load **once** at startup
- ✅ Vector store loaded **once** in memory
- ✅ Direct Python execution - no process spawning
- ✅ **Much faster responses!** 🚀

## 🔧 API Endpoints

### Health Check
```bash
GET http://localhost:8000/api/health
```

### Chat Endpoint
```bash
POST http://localhost:8000/api/chat
Content-Type: application/json

{
  "question": "What is the national language of Pakistan?"
}
```

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'fastapi'"
**Solution:** Install dependencies: `pip install fastapi uvicorn[standard]`

### "Vector store not found"
**Solution:** Make sure you've run `python Legal_RAG_application.py` first to create the vector store

### "Port 8000 already in use"
**Solution:** Change the port in `.env`:
```
PORT=8001
```

### "CORS errors"
**Solution:** The CORS middleware is already configured. If issues persist, check the frontend API_URL setting.

## 📝 Environment Variables

Your `.env` file should have:
```env
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_key
PORT=8000
PDF_PATH=path/to/constitution.pdf
```

## 🚀 Production Deployment

For Vercel deployment, we'll need to update the configuration. FastAPI works great with Vercel's Python runtime!

---

**Enjoy the faster responses!** ⚡

