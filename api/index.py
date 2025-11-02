"""
Vercel serverless function handler for FastAPI
This allows FastAPI to run on Vercel's serverless infrastructure
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.main import app
from mangum import Mangum

# Create ASGI handler for Vercel
handler = Mangum(app, lifespan="off")

