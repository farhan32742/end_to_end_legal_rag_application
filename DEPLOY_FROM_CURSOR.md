# Deploy to Vercel from Cursor

## 🚀 Quick Deployment Guide

Since you already have GitHub connected to Vercel, you have two options:

## Option 1: Use Vercel Dashboard (Recommended - Easiest)

1. **Go to Vercel Dashboard**: https://vercel.com/dashboard
2. **Select your project** (or create new if needed)
3. **Set Environment Variables**:
   - Go to: Settings → Environment Variables
   - Add:
     - `GROQ_API_KEY` = your key
     - `GOOGLE_API_KEY` = your key
4. **Deploy**:
   - If project is linked to GitHub, it auto-deploys on push
   - Or click "Deploy" button manually
   - Or go to Deployments → "Redeploy"

## Option 2: Use Vercel CLI (Terminal)

### Step 1: Authenticate
```bash
vercel login
```
- This will open browser
- Complete authentication
- Return to terminal

### Step 2: Link Project
```bash
vercel link
```
- Select: "Link to existing project" (if you have one in Vercel)
- Or: "Create new project"
- Select scope/team
- Select project name

### Step 3: Deploy
```bash
vercel --prod
```

## ✅ What's Already Done

- ✅ Code pushed to GitHub
- ✅ `vercel.json` configured correctly
- ✅ All files included (vectorstore, etc.)
- ✅ Ready for deployment

## 🔑 Critical: Environment Variables

**BEFORE deploying, set these in Vercel Dashboard:**
- `GROQ_API_KEY`
- `GOOGLE_API_KEY`

## 📝 Deployment Checklist

- [ ] Environment variables set in Vercel
- [ ] Code pushed to GitHub (✅ Done)
- [ ] Vercel project connected to GitHub repo (✅ Done)
- [ ] Deploy!

## 🎯 After Deployment

Your app will be live at: `https://your-project-name.vercel.app`

---

**Recommended**: Use Option 1 (Dashboard) - it's easier and you're already set up!

