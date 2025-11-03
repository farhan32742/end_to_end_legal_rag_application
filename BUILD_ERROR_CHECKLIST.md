# 🔍 Build Error Checklist

## How to Find the Actual Error

The logs you shared only show **warnings** (yellow text). The actual **error** (red text) appears later in the logs.

### Steps to Find Error:

1. **Scroll down** in the Vercel build logs
2. **Look for red text** or "Error:" messages
3. **Copy the complete error message** (not just warnings)

## Common Errors & Fixes

### Error 1: "ModuleNotFoundError: No module named 'backend'"
**Fix**: The import path in `api/index.py` might be wrong
**Solution**: Already configured correctly ✅

### Error 2: "npm ERR! code ELIFECYCLE" or "Build command failed"
**Cause**: Frontend build failing
**Fix**: 
- Check Node.js version (should be 18+)
- Verify `npm run build` works locally

### Error 3: "Cannot find module" (Python)
**Cause**: Missing dependencies
**Fix**: Verify `requirements.txt` has all packages

### Error 4: "Vector store not found"
**Cause**: Path issue or files missing
**Fix**: Verify `vectorstore/constitution_index/` exists in repo ✅

### Error 5: "Function size exceeds limit"
**Cause**: Vectorstore too large (over 50MB)
**Fix**: Need to use external storage or upgrade plan

### Error 6: "Build timeout"
**Cause**: Build taking too long
**Fix**: This is normal for first build, wait it out

## 📋 What to Share

When sharing the error, please include:
1. **The complete error message** (red text)
2. **Which step failed**: Frontend build or Python function
3. **Line number** where it failed (if shown)

## 🔧 Quick Debug Steps

**In Vercel Dashboard:**
1. Click on the failed deployment
2. Go to **"Build Logs"** tab
3. Scroll to the bottom
4. Look for lines starting with "Error:", "Failed:", or in red color
5. Copy that entire section

---

**Please scroll down and share the actual error message!** 📝

