# ⚡ Quick Start - FastAPI Version

## 🚀 Getting Started (3 Steps!)

### Step 1: Install Dependencies

```bash
pip install fastapi uvicorn[standard] python-multipart mangum
```

Or install everything:
```bash
pip install -r requirements.txt
```

### Step 2: Start Backend (Terminal 1)

**Easiest way:**
```bash
python start_backend.py
```

**Or manual:**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

You'll see:
```
🚀 Initializing RAG Service...
📚 Loading vector store and models...
✅ All models loaded successfully!
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 3: Start Frontend (Terminal 2)

```bash
cd frontend
npm start
```

## 🎯 Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Interactive Swagger UI!)
- **Alternative Docs**: http://localhost:8000/redoc

## ⚡ Why FastAPI is Faster

### Before (Express.js):
```
Request → Node.js → Spawn Python → Load Models → Process → Return
         (slow)     (very slow)    (very slow)
```

### Now (FastAPI):
```
Request → Python (Models Already Loaded) → Process → Return
         (instant!)     (fast!)
```

**Key Optimization:** All models (LLM, embeddings, vector store) load **once** at startup, not on every request!

## 🎨 Test It

1. Open http://localhost:3000
2. Ask: "What is the national language of Pakistan?"
3. **Notice the speed!** ⚡

## 📝 API Usage

### Using curl:
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the national language of Pakistan?"}'
```

### Using Python:
```python
import requests

response = requests.post(
    "http://localhost:8000/api/chat",
    json={"question": "What is the national language of Pakistan?"}
)
print(response.json())
```

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'fastapi'"
```bash
pip install fastapi uvicorn[standard] python-multipart
```

### "Vector store not found"
```bash
python Legal_RAG_application.py
```

### "Port 8000 already in use"
Change port in `.env`:
```
PORT=8001
```

Then restart backend.

## 🎉 Next Steps

- Check out the interactive API docs at http://localhost:8000/docs
- Test different questions
- Deploy to Vercel (see FASTAPI_SETUP.md)

---

**Enjoy the speed boost!** 🚀

