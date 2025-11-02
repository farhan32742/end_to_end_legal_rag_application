# Legal RAG Chatbot

A web application for asking questions about Pakistan's Constitution using Retrieval-Augmented Generation (RAG).

## Project Structure

```
legal_end_to_end_chatbot/
├── backend/                 # FastAPI backend
│   ├── main.py             # FastAPI application
│   ├── services/           # Business logic
│   │   └── rag_service.py   # RAG service (models preloaded)
│   └── __init__.py          # Package initialization
│
├── frontend/               # React application
│   ├── public/            # Static files
│   ├── src/               # React source code
│   │   ├── components/    # React components
│   │   ├── App.js         # Main app component
│   │   └── index.js       # Entry point
│   └── package.json       # Frontend dependencies
│
├── api/                    # Vercel serverless functions
│   └── index.py           # Vercel handler for FastAPI
│
├── Legal_RAG_application.py  # Original Python RAG application
├── start_backend.py        # Quick start script for FastAPI
├── vercel.json             # Vercel deployment configuration
└── README.md               # This file
```

## Features

- 🤖 Chat interface for legal questions
- 📚 RAG-based answers from Constitution of Pakistan
- 🎨 Modern, responsive UI
- 🚀 Ready for Vercel deployment

## Setup Instructions

### Prerequisites

1. **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
2. **Python** (v3.8 or higher) - [Download](https://www.python.org/)
3. **npm** (comes with Node.js)

### Installation

1. **Install Backend Dependencies:**
   ```bash
   cd backend
   npm install
   cd ..
   ```

2. **Install Frontend Dependencies:**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

3. **Install Python Dependencies:**
   ```bash
   pip install langchain langchain-community langchain-google-genai langchain-groq faiss-cpu python-dotenv
   ```

4. **Environment Variables:**
   
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_API_KEY=your_google_api_key
   PDF_PATH=path/to/your/constitution.pdf
   PORT=5000
   ```

   For Vercel deployment, add these in Vercel Dashboard → Settings → Environment Variables.

### Running Locally

1. **Start the Backend:**
   ```bash
   cd backend
   npm start
   ```
   The API will run on `http://localhost:5000`

2. **Start the Frontend** (in a new terminal):
   ```bash
   cd frontend
   npm start
   ```
   The app will open at `http://localhost:3000`

### Initializing the Vector Store

Before using the chatbot, you need to create the vector store:

1. Make sure you have your PDF file path set in `.env` as `PDF_PATH`
2. Run the original Python script:
   ```bash
   python Legal_RAG_application.py
   ```
   This will create the `vectorstore/constitution_index` directory.

## Deployment to Vercel

### Method 1: Using Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel
   ```

### Method 2: Using GitHub + Vercel Dashboard

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Add New Project"
4. Import your GitHub repository
5. Add environment variables in Vercel Dashboard
6. Deploy!

### Important Notes for Vercel Deployment

1. **Python Runtime**: Vercel supports Python, but you may need to:
   - Add a `requirements.txt` file for Python dependencies
   - Consider using a serverless function approach for the Python RAG logic

2. **Vector Store**: You'll need to:
   - Upload the `vectorstore` folder to your deployment
   - Or use a cloud storage solution (S3, etc.)

3. **Build Settings**: 
   - Root Directory: `./`
   - Build Command: `cd frontend && npm install && npm run build`
   - Output Directory: `frontend/build`

4. **Environment Variables**: Add all your `.env` variables in Vercel Dashboard

## API Endpoints

- `GET /api/health` - Health check
- `POST /api/chat` - Send a question
  ```json
  {
    "question": "What is the national language of Pakistan?"
  }
  ```

## Technology Stack

- **Frontend**: React.js
- **Backend**: FastAPI (Python)
- **RAG**: LangChain + FAISS + Groq LLM + Google Embeddings
- **Deployment**: Vercel

## Troubleshooting

- **Python script not found**: Make sure Python is in your PATH
- **Vector store not found**: Run the initialization script first
- **API connection errors**: Check that the backend is running and CORS is configured
- **Build errors on Vercel**: Check environment variables and Python dependencies

## License

ISC

