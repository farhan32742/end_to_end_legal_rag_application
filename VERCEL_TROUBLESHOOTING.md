# Vercel Deployment Troubleshooting

## 🔍 What to Check

### 1. **Check Build Logs Completely**
Scroll down past the warnings to see the **actual error**. Common errors:

#### "ModuleNotFoundError" or "ImportError"
- **Cause**: Python dependencies not installing
- **Fix**: Ensure `requirements.txt` is in root directory
- **Verify**: All packages listed in `requirements.txt` are correct

#### "Vector store not found"
- **Cause**: Path issues or files missing
- **Fix**: Verify `vectorstore/constitution_index/` files are in repo
- **Check**: Files `index.faiss` and `index.pkl` exist

#### "Build command failed"
- **Cause**: Frontend build failing
- **Fix**: Test locally: `cd frontend && npm run build`
- **Check**: Node version compatibility

#### "Function timeout" or "Execution timeout"
- **Cause**: RAG service loading takes too long
- **Fix**: Consider lazy loading models (modify `rag_service.py`)

### 2. **Environment Variables**
**MUST be set in Vercel Dashboard:**
- Go to: Project → Settings → Environment Variables
- Add:
  - `GROQ_API_KEY` = (your key)
  - `GOOGLE_API_KEY` = (your key)

### 3. **File Size Limits**
- Vercel free tier: 50MB per function
- Check size of `vectorstore/` folder
- If too large, consider:
  - Upgrading to Pro plan
  - Using external storage (S3, etc.)

### 4. **Build Configuration**
Current `vercel.json`:
- Python function: `api/index.py`
- Frontend build: `frontend/package.json`
- Output: `frontend/build/`

## 🛠️ Quick Fixes

### If Python Dependencies Fail:
```bash
# Test locally first
pip install -r requirements.txt
```

### If Frontend Build Fails:
```bash
# Test locally
cd frontend
npm install
npm run build
```

### If Vectorstore Not Found:
```bash
# Verify files exist
ls -la vectorstore/constitution_index/
# Should show: index.faiss, index.pkl
```

## 📝 Common Error Messages & Solutions

### Error: "Cannot find module 'backend'"
**Solution**: Check that `api/index.py` has correct path setup

### Error: "Mangum not found"
**Solution**: Ensure `mangum` is in `requirements.txt`

### Error: "Build command failed"
**Solution**: Check Node.js version, ensure `npm run build` works locally

### Error: "File size exceeds limit"
**Solution**: Vectorstore too large, use external storage

## 🆘 Next Steps

1. **Share the FULL error message** from Vercel build logs
2. **Verify environment variables** are set
3. **Test build locally** if possible
4. **Check file sizes** (especially vectorstore)

---

**After sharing the full error, we can provide specific fixes!**

