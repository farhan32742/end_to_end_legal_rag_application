from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import uvicorn
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Import RAG service
from services.rag_service import RAGService

# Initialize FastAPI app
app = FastAPI(
    title="Legal RAG Chatbot API",
    description="FastAPI backend for Legal RAG Chatbot",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG service (loads models once at startup for speed)
print("🚀 Initializing RAG Service...")
rag_service = RAGService()
print("✅ RAG Service initialized successfully!")

# Request/Response models
class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    question: str

# API Routes
@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Legal RAG API is running"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat endpoint - receives questions and returns answers"""
    try:
        if not request.question or not request.question.strip():
            raise HTTPException(status_code=400, detail="Question is required")
        
        # Get answer from RAG service
        answer = await rag_service.get_answer(request.question.strip())
        
        return ChatResponse(
            answer=answer,
            question=request.question
        )
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process question: {str(e)}"
        )

# Serve React frontend in production
frontend_build_path = Path(__file__).parent.parent / "frontend" / "build"

if frontend_build_path.exists():
    # Serve static files
    app.mount("/static", StaticFiles(directory=frontend_build_path / "static"), name="static")
    
    # Serve React app for all other routes
    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        """Serve React app for all routes"""
        if full_path.startswith("api") or full_path.startswith("static"):
            raise HTTPException(status_code=404)
        
        index_file = frontend_build_path / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        raise HTTPException(status_code=404)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,  # Set to False in production
        log_level="info"
    )

