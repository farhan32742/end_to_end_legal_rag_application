# Vercel Deployment Setup Guide

## ✅ Configuration Updated

The `vercel.json` has been configured for:
- Python FastAPI backend (serverless function)
- React frontend (static build)

## 🔑 Critical: Environment Variables

You **MUST** add these environment variables in Vercel Dashboard:

1. Go to your Vercel project → **Settings** → **Environment Variables**
2. Add the following:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

## 📦 What Gets Deployed

✅ **Included:**
- Backend Python code (`backend/`, `api/`)
- Frontend React app (`frontend/`)
- Vectorstore files (`vectorstore/constitution_index/`)
- All configuration files

## 🔍 Deployment Steps

1. **Ensure Environment Variables are set** (see above)
2. **Push code to GitHub** (already done ✅)
3. **Vercel will auto-deploy** when it detects the push
4. **Monitor build logs** in Vercel Dashboard

## 🐛 Common Issues

### Build Fails:
- Check that environment variables are set correctly
- Verify `requirements.txt` has all dependencies
- Check build logs for specific errors

### API Not Working:
- Verify environment variables are set
- Check function logs in Vercel Dashboard
- Ensure vectorstore files are in the repo (they are ✅)

### Frontend Not Loading:
- Check that React build completed successfully
- Verify routing in `vercel.json`

## 📝 Notes

- Vectorstore is included in the repo (required for RAG)
- Python dependencies install automatically from `requirements.txt`
- Frontend builds automatically from `frontend/package.json`

---

**After deployment, your app will be live at:** `https://your-project.vercel.app`

