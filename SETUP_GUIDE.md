# 🚀 EduQuiz Pro - Setup Guide

## Quick Start (5 minutes)

### Step 1: Get Your Groq API Key
1. Visit https://console.groq.com/keys
2. Sign up for a free account (or login if you have one)
3. Click "Create API Key"
4. Copy the API key

### Step 2: Setup Environment
```bash
cd /Applications/mcq_generator_llama

# Create .env file
cp .env.example .env

# Edit .env and paste your API key
nano .env
# Add: GROQ_API_KEY=your_api_key_here
```

### Step 3: Run the Application
```bash
source venv/bin/activate
streamlit run app.py
```

### Step 4: Open in Browser
```
http://localhost:8501
```

## 🔑 Groq API Setup (Detailed)

### Free Tier Benefits:
- ✅ Free to use (up to rate limits)
- ✅ Fast inference (Groq is optimized for speed)
- ✅ Access to Mixtral 8x7B model
- ✅ No credit card required for free tier

### How to Get API Key:

1. **Visit Console:**
   - Go to https://console.groq.com

2. **Create Account:**
   - Click "Sign Up" or "Login"
   - Use email/password or Google account
   - Verify email if needed

3. **Navigate to API Keys:**
   - Click on "API Keys" in the left menu
   - Or go directly to https://console.groq.com/keys

4. **Create API Key:**
   - Click "Create API Key"
   - Give it a name (e.g., "EduQuiz Pro")
   - Copy the key (you'll only see it once!)

5. **Add to .env:**
   ```bash
   # Open .env file
   nano /Applications/mcq_generator_llama/.env
   
   # Add or update:
   GROQ_API_KEY=gsk_your_actual_api_key_here
   ```

## ⚙️ Configuration

### Update AI Settings (Optional)

Edit `config.py` to customize:

```python
AI_CONFIG = {
    "model_name": "mixtral-8x7b-32768",  # Current model
    "api_provider": "groq",
    "max_questions": 20,
    "min_questions": 1,
    "default_questions": 5,
    "difficulty_levels": ["Easy", "Medium", "Hard"],
    "timeout": 300
}
```

### Available Groq Models:
- `mixtral-8x7b-32768` (Recommended) - Fast and capable
- `llama2-70b-4096` - Larger model
- `gemma-7b-it` - Smaller, faster

## 🎯 Usage

### First Time Setup:
1. Create an account (Sign Up)
2. Enter email and password
3. Login with your credentials

### Generate MCQs:
1. Enter a topic (e.g., "Python Basics")
2. Select number of questions (1-20)
3. Choose difficulty level (Easy/Medium/Hard)
4. Click "Generate MCQs"
5. Wait for AI to generate (usually 10-30 seconds)

### Save & Export:
1. Review the generated questions
2. Click "Save as PDF" to download
3. PDF automatically saved to `outputs/` folder

### Manage Sessions:
- View all previous MCQ sets in sidebar
- Click any session to reload it
- View your statistics and total questions created

## 🔧 Troubleshooting

### Issue: "GROQ_API_KEY not found"
**Solution:**
```bash
# Check if .env file exists
ls -la .env

# If not, create it:
cp .env.example .env

# Edit and add your key:
nano .env
```

### Issue: "Invalid API Key"
**Solution:**
- Verify API key is correct
- Ensure no extra spaces or newlines
- Generate a new API key if needed

### Issue: "Rate limit exceeded"
**Solution:**
- Wait a few minutes before generating again
- Free tier has rate limits
- Consider upgrading for higher limits

### Issue: "Connection error"
**Solution:**
- Check internet connection
- Verify Groq API is accessible
- Check firewall/proxy settings

## 📊 Performance Tips

### For Faster Generation:
1. Use fewer questions (5-10 is optimal)
2. Be specific with topics
3. Choose "Medium" difficulty
4. Use the Mixtral 8x7B model

### For Better Quality:
1. Use descriptive topics
2. Medium difficulty generally gives best results
3. Don't generate too many questions at once
4. Review and edit generated questions if needed

## 🔐 Security Notes

- **Keep API Key Private:** Never share your API key
- **Use .env File:** Keep sensitive data out of version control
- **Secure Database:** User passwords are hashed with strong algorithms
- **Local Storage:** All data stored locally (no cloud sync)

## 📱 Advanced Usage

### Command Line Start:
```bash
cd /Applications/mcq_generator_llama && source venv/bin/activate && streamlit run app.py
```

### Create Alias (Optional):
```bash
echo 'alias eduquiz="cd /Applications/mcq_generator_llama && source venv/bin/activate && streamlit run app.py"' >> ~/.zshrc
source ~/.zshrc

# Now you can run: eduquiz
```

## 🐛 Debug Mode

If you encounter issues, check logs:

```bash
# Run with verbose output
streamlit run app.py --logger.level=debug

# Check if Groq API is accessible:
python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print('GROQ_API_KEY:', os.getenv('GROQ_API_KEY')[:20] + '...' if os.getenv('GROQ_API_KEY') else 'NOT SET')"
```

## 📞 Support

### Common Issues Checklist:
- ✅ API key is set in .env file
- ✅ Internet connection is active
- ✅ Python 3.9+ is installed
- ✅ All dependencies are installed (`pip install -r requirements.txt`)
- ✅ Virtual environment is activated
- ✅ Streamlit is running on http://localhost:8501

### Getting Help:
1. Check error message carefully
2. Review this setup guide
3. Check Groq API status page
4. Contact Groq support or create GitHub issue

## 🎓 Next Steps

1. ✅ Setup complete - Start generating MCQs!
2. 📚 Explore different topics and difficulty levels
3. 📄 Save PDFs for offline use
4. 💾 Build a library of MCQ sets
5. 🚀 Upgrade to premium if needed for higher limits

Happy question generating! 🎉
