# ⚡ Quick Start - EduQuiz Pro with Groq

## 🎯 What You Need (60 seconds)

1. **Groq API Key** - Get it free at https://console.groq.com/keys
2. **Your .env file** - Already created, just add your API key
3. **Run the app** - One command

---

## 🚀 5-Minute Setup

### Step 1: Get Groq API Key (2 minutes)
```bash
# Visit: https://console.groq.com/keys
# 1. Sign up or login
# 2. Click "Create API Key"
# 3. Copy the key (gsk_... format)
```

### Step 2: Add API Key to .env (1 minute)
```bash
# Edit the .env file
nano /Applications/mcq_generator_llama/.env

# Replace this line:
# GROQ_API_KEY=your_groq_api_key_here
# With your actual key:
# GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
```

### Step 3: Run the App (1 minute)
```bash
cd /Applications/mcq_generator_llama
source venv/bin/activate
streamlit run app.py
```

### Step 4: Open in Browser
```
http://localhost:8501
```

---

## 📱 Using EduQuiz Pro

### First Time:
1. **Sign Up** - Create account with email/password
2. **Login** - Use your credentials

### Generate MCQs:
1. **Enter Topic** - "Python Programming", "Biology", etc.
2. **Select Quantity** - 5-20 questions
3. **Choose Level** - Easy, Medium, or Hard
4. **Click Generate** - Wait 10-30 seconds
5. **Save as PDF** - Download your questions

### Check History:
- All previous MCQs in sidebar
- Click any to reload
- View your statistics

---

## ✅ What's Included

- ✨ Beautiful dark purple theme
- 🎓 Professional MCQ generation
- 📄 PDF export with formatting
- 👤 User accounts & session history
- ⚡ Fast Groq API (free tier)
- 🔐 Secure password storage

---

## 🆘 Troubleshooting

### Error: "GROQ_API_KEY not found"
```bash
# Make sure .env file exists and has your key
cat /Applications/mcq_generator_llama/.env
```

### Error: "Invalid API Key"
```bash
# Get a new key from: https://console.groq.com/keys
# Make sure no extra spaces in .env file
```

### Error: "Connection error"
```bash
# Check internet connection
# Verify Groq API is accessible
# Try opening: https://console.groq.com
```

---

## 💡 Pro Tips

- Start with 5-10 questions for testing
- Be specific with topics for better results
- Medium difficulty usually gives best results
- Save PDFs for offline use
- Check sidebar for your question history

---

## 🔗 Useful Links

- **Groq Console**: https://console.groq.com/keys
- **Groq Docs**: https://console.groq.com/docs
- **GitHub Repo**: https://github.com/bhanumgowda/mcq-generator-llama

---

## 📞 Need Help?

1. **Check SETUP_GUIDE.md** - Comprehensive setup documentation
2. **Check README.md** - Feature documentation
3. **Review .env.example** - Configuration example

---

**Ready to generate amazing MCQs? Start now!** 🚀✨
