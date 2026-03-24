# 🎓 EduQuiz Pro - ChatGPT Reference Card

Copy this when asking ChatGPT about the project:

---

## PROJECT DETAILS

**Name**: EduQuiz Pro v1.0.0  
**Type**: AI-Powered MCQ Generator  
**Status**: Production Ready  
**Tech Stack**: Python 3.13 + Streamlit + Groq API

---

## KEY FEATURES

✅ AI-powered MCQ generation using Groq Llama 3.3-70B  
✅ Modern dark theme UI (Purple/Dark Navy)  
✅ User authentication & session management  
✅ Professional PDF export  
✅ Session history & statistics  
✅ 1-20 questions per set, 3 difficulty levels

---

## ARCHITECTURE

- **Frontend**: Streamlit web app (361 lines)
- **Backend**: Python with SQLite database
- **AI**: Groq API integration via LangChain
- **PDF**: ReportLab professional generation
- **Config**: Centralized in config.py (326 lines)

---

## FILES & STRUCTURE

```
app.py                  - Main application (361 lines)
config.py               - Configuration (326 lines)
auth.py                 - Authentication & database
pdf_generator.py        - PDF creation
prompt.py               - Prompt engineering
requirements.txt        - Dependencies
Dockerfile              - Container image
docker-compose.yml      - Docker compose
.env                    - API keys (Groq)
AWS_DEPLOYMENT.md       - Deployment guide
```

---

## DEPLOYMENT OPTIONS

1. **AWS App Runner** (Easiest)
   - Zero config, auto-scaling
   - $1-7/month
   - 5-10 min setup

2. **AWS EC2 + Docker**
   - Full control
   - $11-18/month
   - 15-20 min setup

3. **AWS ECS Fargate**
   - Managed containers
   - $64-66/month
   - 20-30 min setup

---

## TECH STACK DETAILS

| Component | Technology |
|-----------|-----------|
| Framework | Streamlit 1.54.0 |
| Language | Python 3.13 |
| AI/LLM | Groq Llama 3.3-70B |
| Database | SQLite3 |
| PDF Gen | ReportLab 4.4.9 |
| Auth | bcrypt |
| Config | python-dotenv |

---

## ENVIRONMENT SETUP

```bash
# Required environment variable:
GROQ_API_KEY=gsk_xxxxxxxxxxxxx  # From console.groq.com/keys
```

---

## COLOR SCHEME (Dark Theme)

```
Primary:    #8B5CF6 (Purple)
Background: #0F172A (Dark Navy)
Text:       #E5E7EB (Light Gray)
Success:    #10B981 (Green)
Error:      #EF4444 (Red)
```

---

## DATABASE SCHEMA

**Users Table**:
- id, email, password (hashed)

**History Table**:
- id, email, topic, mcq_text, pdf_path, created_at

---

## QUICK START (Local)

```bash
cd /Applications/mcq_generator_llama
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
# Open http://localhost:8501
```

---

## PERFORMANCE METRICS

- MCQ Generation: 5-15 seconds
- PDF Export: 1-2 seconds
- Page Load: <1 second
- Memory: 200-400MB
- Container Size: ~500MB

---

## SECURITY FEATURES

✅ Password hashing (bcrypt)  
✅ API keys in .env (not in code)  
✅ SQL injection prevention  
✅ Input validation  
✅ Session management  
✅ Error handling

---

## EXAMPLE WORKFLOW

1. User signs up (email/password)
2. Enters topic: "Python Programming"
3. Selects 10 questions, Medium difficulty
4. Clicks "Generate MCQs"
5. Groq generates questions (10-15s)
6. User exports as PDF
7. Session saved to database
8. Can reload from history

---

## KNOWN LIMITATIONS

⚠️ SQLite (single file database)  
⚠️ Single server (not distributed)  
⚠️ Limited concurrent users (~10-20)  
⚠️ No caching layer  
⚠️ No email delivery for PDFs

---

## FUTURE ENHANCEMENTS

- [ ] Question banks
- [ ] Analytics dashboard
- [ ] Multiple question formats
- [ ] Mobile app
- [ ] Multi-language support
- [ ] Batch PDF export
- [ ] API endpoints

---

## DEPLOYMENT CHECKLIST

- [ ] Create GitHub repository
- [ ] Add Docker files (Dockerfile, .dockerignore)
- [ ] Setup AWS account
- [ ] Configure Groq API key
- [ ] Choose deployment option
- [ ] Setup domain & SSL
- [ ] Monitor logs
- [ ] Setup backups

---

## COMMON QUESTIONS

**Q: How much does it cost?**  
A: $1-7/month (App Runner), $11-18/month (EC2), $64-66/month (Fargate)

**Q: How fast is MCQ generation?**  
A: 5-15 seconds depending on question count and complexity

**Q: Can it scale?**  
A: Yes, with RDS (PostgreSQL) + load balancer + multiple instances

**Q: Is it secure?**  
A: Yes, with bcrypt, environment variables, and input validation

**Q: What's the user limit?**  
A: SQLite supports ~10-20 concurrent, PostgreSQL supports thousands

---

## CONTACT INFO

- **Status**: ✅ Production Ready
- **Last Update**: March 24, 2026
- **License**: MIT
- **Repository**: GitHub (bhanumgowda/mcq-generator-llama)

---

**Use this card to quickly brief ChatGPT or other AI assistants about the project!**
