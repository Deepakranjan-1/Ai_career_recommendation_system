# 🚀 Separate Frontend & Backend Deployment on Render

## Architecture Overview

```
┌─────────────────┐    API Calls    ┌─────────────────┐
│   Frontend      │ ──────────────► │   Backend       │
│   (Static Site) │                 │   (Web Service) │
│   Next.js       │ ◄────────────── │   Flask API     │
└─────────────────┘    JSON Data    └─────────────────┘
```

## 🎯 Step 1: Deploy Backend (Already Done!)

Your Flask API is already deployed:
- **URL**: `https://ai-career-recommendation-system.onrender.com`
- **Status**: ✅ Working
- **Endpoints**: `/predict`, `/options`, `/health`

## 🎯 Step 2: Deploy Frontend (Next.js Static Site)

### Option A: Deploy to Render Static Site

1. **Create New Service on Render**:
   - Go to [render.com](https://render.com)
   - Click "New +" → "Static Site"
   - Connect your GitHub repository

2. **Configure the Service**:
   ```
   Name: ai-career-frontend
   Branch: main
   Root Directory: career-recommender
   Build Command: npm install && npm run build
   Publish Directory: out
   ```

3. **Add Environment Variable**:
   ```
   NEXT_PUBLIC_API_URL = https://ai-career-recommendation-system.onrender.com
   ```

4. **Deploy**: Click "Create Static Site"

### Option B: Deploy to Vercel (Recommended)

1. **Push to GitHub** (if not already):
   ```bash
   git add .
   git commit -m "Add frontend deployment config"
   git push origin main
   ```

2. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Set **Root Directory**: `career-recommender`
   - Add Environment Variable:
     ```
     NEXT_PUBLIC_API_URL = https://ai-career-recommendation-system.onrender.com
     ```
   - Deploy!

### Option C: Deploy to Netlify

1. **Build locally**:
   ```bash
   cd career-recommender
   npm run build
   ```

2. **Deploy to Netlify**:
   - Drag the `out` folder to [netlify.com/drop](https://netlify.com/drop)
   - Or connect GitHub repository
   - Set build command: `npm run build`
   - Set publish directory: `out`

## 🔗 Connection Configuration

The frontend is already configured to connect to your backend:

**Development**: Uses `http://localhost:5000`
**Production**: Uses `https://ai-career-recommendation-system.onrender.com`

## 🧪 Test the Connection

1. **Test Backend**:
   ```bash
   curl https://ai-career-recommendation-system.onrender.com/health
   ```

2. **Test Frontend**: Once deployed, visit your frontend URL and submit the form

## 📋 Deployment Checklist

### Backend ✅
- [x] Flask API deployed on Render
- [x] CORS enabled for frontend
- [x] All endpoints working
- [x] Environment variables configured

### Frontend 🚀
- [x] Next.js build successful
- [x] Static export configured
- [x] Environment variables set
- [x] API URL configured
- [ ] Deploy to hosting platform
- [ ] Test form submission

## 🎉 Expected Result

After deployment:
- **Backend**: `https://ai-career-recommendation-system.onrender.com` (API only)
- **Frontend**: `https://your-frontend-url.com` (Full web interface)
- **Connection**: Frontend calls backend API seamlessly

## 🔧 Troubleshooting

### CORS Issues
If you get CORS errors, ensure your Flask app has:
```python
from flask_cors import CORS
CORS(app)  # This allows all origins
```

### API Connection Issues
Check the browser console for errors and verify:
1. Backend is responding: `/health` endpoint
2. Environment variable is set correctly
3. No typos in the API URL

## 🚀 Quick Deploy Commands

```bash
# Backend (already deployed)
git push origin main  # Triggers auto-deploy on Render

# Frontend - Vercel
npx vercel --prod

# Frontend - Manual build
cd career-recommender
npm run build
# Upload 'out' folder to your hosting platform
```

Your separate deployment is ready! 🎯