"""
Quick start script for FastAPI backend
Run this from the project root: python start_backend.py
"""
import uvicorn
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    # Get paths
    project_root = Path(__file__).parent.absolute()
    backend_path = project_root / "backend"
    
    # Load .env from project root if it exists
    env_file = project_root / ".env"
    if env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)
    
    # Get port from environment or use default
    port = int(os.getenv("PORT", 8000))
    
    print(f"🚀 Starting FastAPI server on port {port}...")
    print(f"📖 API docs will be available at: http://localhost:{port}/docs")
    print(f"🎯 API endpoint: http://localhost:{port}/api/chat")
    print(f"📁 Backend path: {backend_path}")
    print(f"💡 Tip: If you get import errors, run: cd backend && uvicorn main:app --reload")
    print()
    
    # Add backend to Python path
    if str(backend_path) not in sys.path:
        sys.path.insert(0, str(backend_path))
    
    # Change to backend directory
    original_dir = os.getcwd()
    os.chdir(backend_path)
    
    try:
        # Import app directly to check for errors
        import main
        print("✅ Successfully imported main module")
        print()
        
        # Run uvicorn with import string (enables reload functionality)
        # Since we're already in backend directory, "main:app" will work
        uvicorn.run(
            "main:app",  # Use import string for reload to work
            host="0.0.0.0",
            port=port,
            reload=True,
            reload_dirs=[str(backend_path)],
            log_level="info"
        )
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print(f"💡 Try running manually: cd backend && python -m uvicorn main:app --reload")
        sys.exit(1)
    finally:
        os.chdir(original_dir)

