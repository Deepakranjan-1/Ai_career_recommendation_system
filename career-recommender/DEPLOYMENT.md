# 🚀 Frontend Deployment Guide

## Quick Deploy Options

### Option 1: Vercel (Recommended)
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your repository
4. Set environment variable:
   - `NEXT_PUBLIC_API_URL` = `https://ai-career-recommendation-system.onrender.com`
5. Deploy!

### Option 2: Netlify
1. Build the project: `npm run build`
2. Upload the `out` folder to Netlify
3. Set environment variable in Netlify dashboard

### Option 3: Render Static Site
1. Create new Static Site on Render
2. Connect your GitHub repo
3. Set build command: `npm run build`
4. Set publish directory: `out` or `.next`
5. Add environment variable

## Environment Variables

Create `.env.local` in the root:
```
NEXT_PUBLIC_API_URL=https://ai-career-recommendation-system.onrender.com
```

## Local Development

1. Install dependencies:
```bash
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Open http://localhost:3000

## Build for Production

```bash
npm run build
npm start
```

## API Integration

The frontend automatically connects to:
- **Production**: Your Render API URL
- **Development**: localhost:5000

No code changes needed between environments!