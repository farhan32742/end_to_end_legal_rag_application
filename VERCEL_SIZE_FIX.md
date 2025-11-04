# 🔧 Vercel Serverless Function Size Fix

## Problem
Your Vercel deployment was failing with:
```
Error: A Serverless Function has exceeded the unzipped maximum size of 250 MB
```

## ✅ Solutions Applied

### 1. Created `.vercelignore` File
This excludes large files and unnecessary assets from the serverless function bundle:
- PDF files (not needed if vectorstore exists)
- Documentation files (*.md)
- Python cache files (__pycache__)
- Development scripts (*.sh, *.bat)
- IDE files
- Log files

### 2. Updated `vercel.json`
Added `functions` configuration to explicitly exclude files from the Python function bundle:
```json
"functions": {
  "api/**": {
    "excludeFiles": [
      "**/*.pdf",
      "**/*.md",
      "**/__pycache__/**",
      "frontend/**",
      ...
    ]
  }
}
```

## 📦 What's Likely Causing the Size Issue

The main contributors to the large bundle size are:

1. **`faiss-cpu`** - This package is HUGE (often 100+ MB)
   - Required for FAISS vector stores
   - No easy way around it if using FAISS

2. **LangChain packages** - Can be large (50-100 MB combined)
   - `langchain`, `langchain-community`, `langchain-google-genai`, `langchain-groq`

3. **Vectorstore files** - Your FAISS index files
   - `vectorstore/constitution_index/index.faiss`
   - `vectorstore/constitution_index/index.pkl`

## 🚀 Next Steps

### Step 1: Try Deploying Again
The `.vercelignore` and `vercel.json` changes should significantly reduce the bundle size. Try deploying again.

### Step 2: If Still Too Large - Consider These Options

#### Option A: Remove Unused Dependencies
Since your vectorstore already exists, you might not need `pypdf` in production:
```bash
# Remove from requirements.txt if not needed
# pypdf  # Only needed to create vectorstore, not to run it
```

#### Option B: Use External Storage for Vectorstore
If the vectorstore files are large, move them to external storage:
- **Vercel Blob Storage** (paid feature)
- **AWS S3** (free tier available)
- **Google Cloud Storage**
- **Cloudflare R2** (free tier available)

Then modify `rag_service.py` to download the vectorstore on first request instead of bundling it.

#### Option C: Use Lighter Vector Store Alternative
Consider switching from FAISS to a lighter alternative:
- **Chroma** (lighter than FAISS)
- **Pinecone** (cloud-based, free tier)
- **Weaviate** (cloud-based)

#### Option D: Upgrade Vercel Plan
- Pro plan has higher limits
- Enterprise plan has even more flexibility

## 📊 How to Check Bundle Size Locally

To check what's taking up space before deploying:

```bash
# Install vercel CLI
npm i -g vercel

# Build locally to see size
vercel build
```

## ⚠️ Important Notes

1. **Vectorstore Must Be Included**: The vectorstore files (`vectorstore/constitution_index/`) MUST be included in the deployment for the app to work. They are NOT excluded by `.vercelignore`.

2. **Python Dependencies**: The Python dependencies (especially `faiss-cpu`) are the main size contributors. These are necessary for the app to function.

3. **Frontend is Separate**: The frontend build is handled separately and doesn't affect the Python function size.

## 🎯 Expected Results

After these changes:
- ✅ Large PDF files excluded
- ✅ Documentation files excluded
- ✅ Development files excluded
- ✅ Python cache files excluded
- ✅ Frontend files excluded from Python function

The bundle should now be significantly smaller. If it's still over 250 MB, the main culprit is likely `faiss-cpu` + LangChain packages, which are essential for your app to function.

## 🔍 If Still Failing

If the deployment still fails after these changes:

1. **Check the build logs** in Vercel dashboard to see the exact size
2. **Consider moving vectorstore to external storage** (Option B above)
3. **Consider using a lighter vector store** (Option C above)
4. **Contact Vercel support** if you need assistance with Pro plan upgrade

