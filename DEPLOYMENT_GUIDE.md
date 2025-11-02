# Deployment Guide for Legal RAG Chatbot

## 📋 Overview

This guide will help you deploy your Legal RAG Chatbot on Vercel. Since you're new to these frameworks, I'll explain everything step by step.

## 🏗️ What We Built

### **Frontend (React)**
- Location: `frontend/` folder
- What it does: The user interface where users type questions and see answers
- Technology: React.js - a JavaScript library for building user interfaces

### **Backend (FastAPI/Python)**
- Location: `backend/` folder  
- What it does: Receives questions from frontend, processes with RAG, returns answers
- Technology: FastAPI (Python) - fast, modern API framework with preloaded models

### **Python RAG Logic**
- Location: `backend/services/rag_service.py`
- What it does: Your RAG application that processes legal questions (models preloaded for speed)
- Technology: LangChain + FAISS + Groq LLM + Google Embeddings

## 🚀 Step-by-Step Deployment

### **Step 1: Install Dependencies Locally First**

Before deploying, test everything locally:

#### 1.1 Install Backend Dependencies (Python/FastAPI)
```bash
pip install -r requirements.txt
```

#### 1.2 Install Frontend Dependencies
```bash
cd frontend
npm install
cd ..
```

### **Step 2: Set Up Environment Variables**

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
PDF_PATH=path/to/your/constitution.pdf
PORT=5000
```

**Important:** Never commit `.env` to Git! It's already in `.gitignore`.

### **Step 3: Initialize Vector Store**

Before deployment, create your vector store:

```bash
python Legal_RAG_application.py
```

This creates `vectorstore/constitution_index/` folder. **You'll need to upload this folder to Vercel** (see Step 5).

### **Step 4: Test Locally**

#### 4.1 Start Backend (FastAPI)
```bash
python start_backend.py
```
**Or manually:**
```bash
cd backend
uvicorn main:app --reload --port 5000
```
Keep this terminal open - backend runs on `http://localhost:5000`

#### 4.2 Start Frontend (New Terminal)
```bash
cd frontend
npm start
```
Frontend opens at `http://localhost:3000`

#### 4.3 Test the App
- Open `http://localhost:3000`
- Type a question about Pakistan's Constitution
- Check if you get an answer

### **Step 5: Prepare for Vercel Deployment**

#### Option A: Using Vercel CLI (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login:**
   ```bash
   vercel login
   ```

3. **Link Your Project:**
   ```bash
   vercel link
   ```

4. **Set Environment Variables:**
   ```bash
   vercel env add GROQ_API_KEY
   vercel env add GOOGLE_API_KEY
   vercel env add PDF_PATH
   ```

5. **Upload Vector Store:**
   - Vercel has a 50MB limit per function
   - If your vectorstore is small (<50MB), you can include it in the repo
   - Otherwise, consider using cloud storage (AWS S3, Google Cloud Storage)

6. **Deploy:**
   ```bash
   vercel --prod
   ```

#### Option B: Using GitHub + Vercel Dashboard (Easier for Beginners)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin your_github_repo_url
   git push -u origin main
   ```

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/Login (use GitHub account for easy integration)
   - Click "Add New Project"
   - Import your GitHub repository

3. **Configure Project:**
   - **Framework Preset:** Other
   - **Root Directory:** `./` (keep as is)
   - **Build Command:** `cd frontend && npm install && npm run build`
   - **Output Directory:** `frontend/build`
   - **Install Command:** (leave empty - Vercel auto-detects)

4. **Add Environment Variables:**
   - In Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add:
     - `GROQ_API_KEY` = your key
     - `GOOGLE_API_KEY` = your key
     - `PDF_PATH` = path to your PDF (or remove if using vectorstore)

5. **Handle Vector Store:**
   - **Small vectorstore (<50MB):**
     - Commit it to GitHub (remove from `.gitignore` temporarily)
     - It will be deployed automatically
   
   - **Large vectorstore (>50MB):**
     - Use Vercel's file storage or external storage
     - Or use Vercel Blob Storage (paid feature)

6. **Deploy:**
   - Click "Deploy" button
   - Wait for build to complete
   - Your app will be live!

## 🔧 Vercel Configuration Explained

The `vercel.json` file tells Vercel how to build and route your app:

- **`/api/chat`** → Routes to Python serverless function
- **`/*`** → Routes to React frontend

## ⚠️ Important Considerations for Vercel

### 1. **Python on Vercel**
- Vercel supports Python serverless functions
- Maximum execution time: 10 seconds (Pro plan: 60 seconds)
- Maximum size: 50MB per function

### 2. **Vector Store Storage**
- If your FAISS index is large, consider:
  - **Vercel Blob Storage** (recommended)
  - **AWS S3** (free tier available)
  - **Google Cloud Storage**

### 3. **Alternative: Hybrid Deployment**
If Vercel's Python limitations are an issue:
- **Frontend on Vercel** (React)
- **Backend on Railway/Render/Heroku** (Node.js + Python)
- Update `API_URL` in frontend

## 🐛 Troubleshooting

### "Vector store not found"
- Ensure `vectorstore/` folder is in your repository
- Check path in Python script matches deployment structure

### "Python dependencies not found"
- Ensure `requirements.txt` is in the root directory (already created)
- Vercel automatically installs Python dependencies from `requirements.txt`
- Make sure `mangum` is included (required for FastAPI on Vercel)

### "API endpoint not working"
- Check Vercel function logs in dashboard
- Verify environment variables are set
- Check CORS settings

### "Build fails"
- Check Node.js version (Vercel uses latest LTS)
- Verify all dependencies in `package.json` files
- Check build logs in Vercel dashboard

## 📚 Next Steps

1. **Test locally** before deploying
2. **Start with Vercel CLI** for easier debugging
3. **Monitor logs** in Vercel dashboard
4. **Consider upgrading** to Vercel Pro for longer execution times if needed

## 🆘 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **React Docs:** https://react.dev

---

**Remember:** Always test locally first! It's much easier to debug on your machine than on Vercel.

