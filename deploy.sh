#!/bin/bash
# Vercel Deployment Script

echo "🚀 Starting Vercel Deployment..."

# Step 1: Login (if not already logged in)
echo "📝 Step 1: Checking Vercel authentication..."
vercel whoami || vercel login

# Step 2: Link project (if not already linked)
echo "🔗 Step 2: Linking project..."
vercel link --yes

# Step 3: Deploy
echo "📦 Step 3: Deploying to Vercel..."
vercel --prod

echo "✅ Deployment complete!"

