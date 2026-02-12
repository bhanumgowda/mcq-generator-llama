# 🎓 EduQuiz Pro - AI MCQ Generator

A professional, AI-powered Multiple Choice Question (MCQ) generator built with Streamlit and powered by Ollama's Llama3 model.

## ✨ Features

### 🎨 Professional UI/UX
- **Modern Design**: Clean, professional interface with gradient themes
- **Responsive Layout**: Wide layout with optimized sidebar navigation
- **Interactive Elements**: Professional cards, metrics, and visual feedback
- **Custom Styling**: Professional color scheme and typography
- **Progress Indicators**: Real-time progress bars during generation

### 🤖 AI-Powered Generation
- **Advanced Prompting**: Intelligent prompt engineering for high-quality questions
- **Multiple Difficulty Levels**: Easy, Medium, and Hard options
- **Flexible Question Count**: Generate 1-20 questions per session
- **Educational Focus**: Questions designed for genuine learning assessment

### 👤 User Management
- **Secure Authentication**: Email-based login and signup system
- **Session Management**: Persistent user sessions with secure logout
- **User Dashboard**: Personal statistics and session overview

### 📚 History & Management
- **Session History**: Save and reload previous MCQ generations
- **Smart Organization**: Sessions organized by topic and date
- **Quick Access**: One-click loading of previous sessions

### 📄 Professional PDF Export
- **Beautiful Layout**: Professional PDF formatting with headers and styling
- **Rich Content**: Includes metadata, timestamps, and user information
- **Organized Structure**: Clear question formatting with proper spacing
- **Branded Design**: EduQuiz Pro branding and footer information

### 🔧 Technical Features
- **Error Handling**: Comprehensive error management and user feedback
- **Performance**: Optimized for speed and reliability
- **Extensible**: Modular architecture for easy feature additions

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Ollama installed with Llama3 model
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mcq_generator_llama
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and setup Ollama:**
   ```bash
   # Install Ollama (visit https://ollama.ai for platform-specific instructions)
   # Pull the Llama3 model
   ollama pull llama3
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

6. **Access the application:**
   Open your browser and navigate to `http://localhost:8501`

## 🎯 How to Use

### 1. **Login/Signup**
- Create a new account or login with existing credentials
- Secure email-based authentication system

### 2. **Generate MCQs**
- Enter your topic (e.g., "Python Programming", "World History")
- Select number of questions (1-20)
- Choose difficulty level (Easy/Medium/Hard)
- Click "Generate MCQs" and wait for AI processing

### 3. **Review and Save**
- Review the generated questions and answers
- Save as PDF for offline use
- Questions are automatically saved to your history

### 4. **Manage Sessions**
- Access previous sessions from the sidebar
- View your generation statistics
- Reload any previous MCQ set with one click

## 🛠️ Technical Architecture

### Frontend
- **Streamlit**: Modern web framework for the user interface
- **Custom CSS**: Professional styling and responsive design
- **Interactive Components**: Forms, progress bars, and dynamic content

### Backend
- **SQLite**: Local database for user management and history
- **Secure Authentication**: Password hashing and session management
- **File Management**: Organized PDF storage in outputs directory

### AI Integration
- **Langchain-Ollama**: Integration with Ollama's Llama3 model
- **Intelligent Prompting**: Sophisticated prompt engineering for quality
- **Error Handling**: Robust error management for AI operations

### PDF Generation
- **ReportLab**: Professional PDF creation and styling
- **Custom Formatting**: Structured layout with metadata
- **Brand Consistency**: Professional branding and design

## 📁 Project Structure

```
mcq_generator_llama/
├── app.py              # Main Streamlit application
├── auth.py             # Authentication and database functions
├── pdf_generator.py    # Professional PDF generation
├── prompt.py           # AI prompt engineering
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml    # Streamlit configuration
├── outputs/           # Generated PDF storage
└── venv/             # Virtual environment
```

## 🎨 UI/UX Improvements

### Design Elements
- **Gradient Headers**: Eye-catching gradient text effects
- **Feature Cards**: Highlighted capability showcases
- **Metric Dashboard**: User statistics and session overview
- **Professional Forms**: Clean input forms with validation
- **Interactive Feedback**: Real-time status updates and animations

### User Experience
- **Intuitive Navigation**: Clear user journey and flow
- **Helpful Tips**: Contextual help and guidance
- **Error Prevention**: Input validation and user guidance
- **Visual Feedback**: Loading states, success messages, and error handling

## 🔧 Configuration

### Streamlit Config (.streamlit/config.toml)
- **Theme**: Professional color scheme
- **Performance**: Optimized server settings
- **Security**: CSRF protection configuration

### Environment Variables
- No additional environment variables required
- All configuration handled through files

## 🚀 Future Enhancements

### Planned Features
- **Question Banks**: Save and categorize question sets
- **Analytics Dashboard**: Detailed usage statistics
- **Export Formats**: Multiple export options (Word, Excel, etc.)
- **Collaboration**: Share question sets with others
- **Question Types**: Support for different question formats

### Technical Improvements
- **Cloud Deployment**: Ready for cloud hosting
- **Database Migration**: PostgreSQL for production
- **API Integration**: RESTful API for external access
- **Performance Optimization**: Caching and optimization

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, please open an issue on GitHub or contact the development team.

---

**EduQuiz Pro** - Revolutionizing education through AI-powered assessment tools. 🎓✨
