# 🚀 Render Deployment Guide

## Files Fixed for Deployment

✅ **app.py** - Updated to use PORT environment variable  
✅ **Procfile** - Changed to use gunicorn  
✅ **render.yaml** - Updated start command  
✅ **requirements.txt** - Fixed scikit-learn version compatibility  

## Deployment Steps

### 1. Push to GitHub ok
```bash
git add .
git commit -m "Fix Render deployment configuration"
git push origin main
```

### 2. Deploy on Render

1. Go to [render.com](https://render.com) and sign in
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `ai-career-recommendation`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Plan**: Free

### 3. Environment Variables (Optional)
No additional environment variables needed for basic deployment.

### 4. Test Deployment

Once deployed, test these endpoints:
- `GET /` - API info
- `GET /health` - Health check  
- `GET /options` - Form options
- `POST /predict` - Career prediction

## Common Issues & Solutions

### Issue 1: Models not loading
**Solution**: All .pkl files are included and verified ✅

### Issue 2: Port binding errors  
**Solution**: Updated app.py to use $PORT environment variable ✅

### Issue 3: Gunicorn vs Waitress
**Solution**: Switched to gunicorn for better Render compatibility ✅

### Issue 4: Scikit-learn version mismatch
**Solution**: Updated requirements.txt to use scikit-learn==1.7.2 ✅

## Test Locally First

Run this before deploying:
```bash
python verify_models.py
python app.py
# In another terminal:
python test_deployment.py
```

## Expected Deployment Time
- Build: 2-3 minutes
- First deploy: 3-5 minutes
- Subsequent deploys: 1-2 minutes

## Post-Deployment

Your API will be available at:
`https://your-service-name.onrender.com`

Update your Next.js frontend to use this URL instead of localhost:5000.