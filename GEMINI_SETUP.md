# 🤖 Google Gemini AI Chatbot Setup Guide

## Step 1: Install Google Gemini API
```bash
pip install google-generativeai
```

## Step 2: Get Free API Key
1. Go to: https://ai.google.dev/
2. Click "Get API Key"
3. Sign in with Google account
4. Create new project or select existing
5. Copy your API key

## Step 3: Set Environment Variable

### Windows:
```cmd
set GEMINI_API_KEY=your-api-key-here
```

### Linux/Mac:
```bash
export GEMINI_API_KEY=your-api-key-here
```

### Or create .env file:
```
GEMINI_API_KEY=your-api-key-here
```

## Step 4: Test the Chatbot
1. Start Django server: `python manage.py runserver`
2. Visit: `http://localhost:8000/chatbot/`
3. Ask any programming question!

## 🎯 Example Questions to Try:
- "How do I learn Python programming?"
- "Explain binary search algorithm"
- "What are coding best practices?"
- "Help me with debugging techniques"
- "Prepare me for coding interviews"

## 🆓 Free Tier Limits:
- 15 requests per minute
- 1,500 requests per day
- Perfect for learning and small projects!

## 🔧 Troubleshooting:
- If API fails, fallback responses will work
- Check your API key is correct
- Ensure internet connection
- Free tier has rate limits

## 🚀 Features:
✅ Real-time AI responses
✅ Programming-focused assistant
✅ Fallback responses (always works)
✅ Modern chat interface
✅ Mobile-friendly design