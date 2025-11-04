# 🚀 Deploy via Vercel Dashboard - Step by Step

Since your Vercel Dashboard is open, follow these steps:

## Step 1: Create New Project

1. Click **"Add New..."** or **"New Project"** button
2. Select your GitHub repository: **`end_to_end_legal_rag_application`**
3. Click **"Import"**

## Step 2: Configure Project Settings

On the import screen:

### Framework Preset
- Select: **"Other"** (or "Vite" if available, but "Other" is fine)

### Root Directory
- Keep: `./` (default)

### Build and Output Settings
- **Build Command**: Leave EMPTY (handled by `vercel.json`)
- **Output Directory**: Leave EMPTY (handled by `vercel.json`)
- **Install Command**: Leave EMPTY (auto-detected)

**Important:** Don't override these - `vercel.json` handles everything!

## Step 3: Environment Variables ⚠️ CRITICAL

**Before clicking Deploy**, add environment variables:

1. Click **"Environment Variables"** section
2. Add these two:

### Variable 1:
- **Key**: `GROQ_API_KEY`
- **Value**: (paste your Groq API key)
- **Environments**: Check all (Production, Preview, Development)

### Variable 2:
- **Key**: `GOOGLE_API_KEY`
- **Value**: (paste your Google API key)
- **Environments**: Check all (Production, Preview, Development)

3. Click **"Save"** after adding each

## Step 4: Deploy

1. Click **"Deploy"** button
2. Wait for build to complete (takes 2-5 minutes)
3. You'll get a live URL like: `https://your-project.vercel.app`

## ✅ What Gets Deployed

- ✅ FastAPI backend (Python serverless functions)
- ✅ React frontend (built and served)
- ✅ Vectorstore files (included in repo)
- ✅ All dependencies

## 🐛 If Build Fails

1. Check **Build Logs** tab
2. Look for error messages (scroll past warnings)
3. Common issues:
   - Missing environment variables → Add them!
   - Python import errors → Check `requirements.txt`
   - Vectorstore not found → Verify files are in repo (they are ✅)

## 📝 After Deployment

Your app will be live at: `https://your-project-name.vercel.app`

**Test it:**
- Frontend: Opens automatically
- API: `https://your-project-name.vercel.app/api/health`

---

**Ready? Follow the steps above in your Vercel Dashboard!** 🎯

