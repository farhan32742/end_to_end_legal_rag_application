# 🚀 Fresh Vercel Deployment - Step by Step

## ✅ Pre-Deployment Checklist

- [x] Code is pushed to GitHub
- [x] `vercel.json` is configured
- [x] `requirements.txt` has all dependencies
- [x] Vectorstore files are in the repo

## 📋 Step-by-Step Deployment

### Step 1: Login to Vercel CLI

```bash
vercel login
```

**What happens:**
- Browser will open
- Authorize Vercel to access your account
- Return to terminal when done

### Step 2: Link Your Project

```bash
vercel link
```

**When prompted:**
1. **"Set up and deploy"?** → Type `Y` (Yes)
2. **"Which scope?"** → Select your account
3. **"Link to existing project?"** → Type `N` (No, create new)
4. **"What's your project's name?"** → Type: `legal-rag-chatbot` (or press Enter for default)
5. **"In which directory is your code located?"** → Type: `./` (or press Enter)

### Step 3: Add Environment Variables

Before deploying, add your API keys:

```bash
vercel env add GROQ_API_KEY
# Paste your Groq API key when prompted
# Select: Production, Preview, Development (or just Production)

vercel env add GOOGLE_API_KEY
# Paste your Google API key when prompted
# Select: Production, Preview, Development (or just Production)
```

### Step 4: Deploy to Production

```bash
vercel --prod
```

This will:
- Build your frontend (React)
- Set up your Python serverless functions
- Deploy everything
- Give you a live URL!

## 🎯 Expected Output

After `vercel --prod`, you'll see:
```
✅ Production: https://your-project-name.vercel.app
```

## 🔧 Alternative: Deploy via GitHub (Recommended)

If you prefer using the Vercel Dashboard:

1. **Go to**: https://vercel.com/new
2. **Import Git Repository**: Select `end_to_end_legal_rag_application`
3. **Configure Project**:
   - Framework Preset: **Other**
   - Root Directory: `./` (keep default)
   - Build Command: (leave empty - handled by vercel.json)
   - Output Directory: (leave empty - handled by vercel.json)
4. **Environment Variables**:
   - Add `GROQ_API_KEY`
   - Add `GOOGLE_API_KEY`
5. **Deploy**: Click "Deploy"

## 🐛 Troubleshooting

### If login fails:
- Make sure you have a Vercel account at https://vercel.com
- Try: `vercel login --github` (if you have GitHub auth)

### If build fails:
- Check that all files are pushed to GitHub
- Verify environment variables are set
- Check build logs in Vercel dashboard

### If API doesn't work:
- Verify environment variables are set
- Check function logs: `vercel logs`
- Ensure vectorstore files are in repo

## 📝 Quick Commands Reference

```bash
# Login
vercel login

# Link project
vercel link

# Add environment variable
vercel env add VARIABLE_NAME

# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# List projects
vercel ls
```

---

**Ready? Let's start with Step 1!** 🚀

