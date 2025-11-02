# 🚀 Quick Start Guide - Legal RAG Chatbot

## Welcome! 👋

This guide will help you get your Legal RAG Chatbot running quickly. Don't worry if you're new to React and Node.js - I'll explain everything!

## 📁 What's in This Project?

```
legal_end_to_end_chatbot/
│
├── 📂 backend/              ← FastAPI Backend (Python)
│   ├── main.py              ← FastAPI server (handles API requests)
│   └── services/            ← Business logic
│       └── rag_service.py   ← Optimized RAG service (preloads models)
│
├── 📂 frontend/             ← React User Interface
│   ├── src/
│   │   ├── components/      ← Chat interface component
│   │   ├── App.js          ← Main React app
│   │   └── index.js        ← Entry point
│   └── public/             ← Static files
│
├── 📂 api/                  ← Vercel serverless functions
│   └── index.py            ← Vercel handler for FastAPI
│
├── Legal_RAG_application.py ← Your original Python script
├── start_backend.py         ← Quick start script
├── vercel.json              ← Vercel deployment config
└── requirements.txt         ← Python dependencies
```

## 🔧 Step 1: Install Everything

### Prerequisites (Install These First):
1. **Node.js** - [Download here](https://nodejs.org/) (v16 or higher)
2. **Python** - [Download here](https://www.python.org/) (v3.8 or higher)
3. **Git** (optional, for version control)

### Install Dependencies:

Open your terminal/command prompt in the project folder and run:

```bash
# Install all Node.js dependencies (one command!)
npm run install-all
```

This will install:
- Backend dependencies (Express.js, etc.)
- Frontend dependencies (React, etc.)

### Install Python Dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Step 2: Set Up Environment Variables

Create a file named `.env` in the root folder with:

```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
 lenpm
```

**⚠️ Important:** Replace `your_groq_api_key_here` and `your_google_api_key_here` with your actual API keys!

## 📚 Step 3: Create Vector Store

Before you can use the chatbot, you need to create the vector database:

```bash
python Legal_RAG_application.py
```

This will create a folder called `vectorstore/constitution_index/` - this is your knowledge base!

**Note:** This might take a few minutes the first time.

## 🏃 Step 4: Run the Application

You need **TWO terminal windows** running at the same time:

### Terminal 1 - Start FastAPI Backend:
```bash
python start_backend.py
```

Or:
```bash
cd backend
uvicorn main:app --reload --port 8000
```

You should see: `INFO:     Uvicorn running on http://0.0.0.0:8000`

### Terminal 2 - Start Frontend:
```bash
cd frontend
npm start
```

Your browser should automatically open to `http://localhost:3000`

## 🎉 Step 5: Use Your Chatbot!

1. Open `http://localhost:3000` in your browser
2. Type a question like: "What is the national language of Pakistan?"
3. Press Enter or click the send button
4. Get your answer!

## 📦 What Each Part Does:

### **Frontend (React)** 
- **Location:** `frontend/` folder
- **What it does:** The pretty interface you see in the browser
- **Technology:** React.js - makes interactive web pages

### **Backend (FastAPI)**
- **Location:** `backend/` folder
- **What it does:** Receives questions, processes them, sends back answers
- **Technology:** FastAPI (Python) - fast, modern API framework
- **Why FastAPI?** ⚡ Models load once at startup = super fast responses!

### **Python RAG**
- **Location:** `backend/services/rag_service.py`
- **What it does:** Your smart AI that understands legal questions (preloads models for speed)
- **Technology:** LangChain + FAISS + Groq LLM

## 🚀 Deploying to Vercel

Once everything works locally, see `DEPLOYMENT_GUIDE.md` for step-by-step Vercel deployment instructions.

## ❓ Common Issues

### "npm: command not found"
- **Solution:** Install Node.js from nodejs.org

### "python: command not found"
- **Solution:** Install Python from python.org (check "Add Python to PATH" during installation)

### "Vector store not found"
- **Solution:** Run `python Legal_RAG_application.py` first to create the vector store

### "Port 8000 already in use"
- **Solution:** Change `PORT=8001` in `.env` file or use: `uvicorn main:app --port 8001`

### "Module not found" errors
- **Solution:** 
  - For Python: Run `pip install -r requirements.txt`
  - For React: Run `npm install` in the `frontend/` folder

## 🎓 Learning Resources

- **React:** https://react.dev/learn
- **FastAPI:** https://fastapi.tiangolo.com/
- **Python:** https://docs.python.org/3/

## 💡 Tips for Beginners

1. **Start Simple:** Get it running locally first before deploying
2. **Read Error Messages:** They usually tell you exactly what's wrong
3. **Test One Thing at a Time:** Don't change multiple things at once
4. **Use Git:** Save your progress with `git commit`
5. **Ask Questions:** Stack Overflow is your friend!

---

**Need help?** Check the `README.md` or `DEPLOYMENT_GUIDE.md` for more details!

