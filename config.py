"""
EduQuiz Pro Configuration Module
Professional configuration management for the MCQ Generator application.
"""

import os
from typing import Dict, Any

class Config:
    """Application configuration class."""
    
    # Application Info
    APP_NAME = "EduQuiz Pro"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "AI-Powered MCQ Generation Platform"
    
    # UI Configuration
    UI_CONFIG = {
        "page_title": f"{APP_NAME} - AI MCQ Generator",
        "page_icon": "🎓",
        "layout": "wide",
        "initial_sidebar_state": "expanded"
    }
    
    # Theme Colors - Modern Dark Theme
    COLORS = {
        "primary": "#8B5CF6",        # Purple
        "secondary": "#A855F7",      # Light Purple
        "accent": "#7C3AED",         # Deep Purple
        "background": "#0F172A",     # Dark Navy
        "secondary_bg": "#1E293B",   # Lighter Dark Navy
        "card_bg": "#334155",        # Medium Dark
        "text": "#E5E7EB",          # Light Gray
        "text_light": "#9CA3AF",    # Medium Gray
        "success": "#10B981",       # Green
        "warning": "#F59E0B",       # Amber
        "error": "#EF4444",         # Red
        "info": "#06B6D4",          # Cyan
        "border": "#475569"         # Dark Border
    }
    
    # Database Configuration
    DATABASE = {
        "name": "users.db",
        "backup_enabled": True,
        "backup_interval": 24  # hours
    }
    
    # AI Model Configuration
    AI_CONFIG = {
        "model_name": "llama3",
        "max_questions": 20,
        "min_questions": 1,
        "default_questions": 5,
        "difficulty_levels": ["Easy", "Medium", "Hard"],
        "timeout": 300  # seconds
    }
    
    # File Storage
    STORAGE = {
        "output_dir": "outputs",
        "pdf_prefix": "mcqs_",
        "max_file_size": 10 * 1024 * 1024,  # 10MB
        "allowed_extensions": [".pdf"]
    }
    
    # Security Settings
    SECURITY = {
        "min_password_length": 6,
        "session_timeout": 3600,  # seconds
        "max_login_attempts": 5
    }
    
    # Professional Messages
    MESSAGES = {
        "welcome": "Welcome to EduQuiz Pro - Your AI-Powered MCQ Generation Platform",
        "login_success": "✅ Login successful! Welcome back!",
        "login_error": "❌ Invalid credentials. Please try again.",
        "signup_success": "✅ Account created successfully! Please login.",
        "signup_error": "❌ User already exists. Please try logging in.",
        "mcq_success": "🎉 MCQs generated successfully!",
        "pdf_success": "✅ PDF saved successfully!",
        "session_loaded": "✅ Previous session loaded successfully!",
        "logout_message": "👋 You have been logged out. Thank you for using EduQuiz Pro!"
    }
    
    # Professional Tips
    TIPS = {
        "topic_tips": [
            "Be specific with your topic for better results",
            "Include context like 'Basic Python Programming' or 'Advanced Calculus'",
            "Topics work best when they're focused on a single subject area"
        ],
        "difficulty_tips": {
            "Easy": "Basic concepts and definitions",
            "Medium": "Applied knowledge and problem-solving",
            "Hard": "Complex analysis and evaluation"
        },
        "question_tips": [
            "Start with 5-10 questions for testing",
            "More questions take longer to generate",
            "Quality over quantity - fewer good questions are better"
        ]
    }
    
    @classmethod
    def get_css_styles(cls) -> str:
        """Get custom CSS styles for the application."""
        return f"""
        <style>
            /* Dark Theme Base */
            .stApp {{
                background-color: {cls.COLORS['background']};
                color: {cls.COLORS['text']};
            }}
            
            .main-header {{
                text-align: center;
                color: {cls.COLORS['primary']};
                font-size: 3.5rem;
                font-weight: bold;
                margin-bottom: 0.8rem;
                background: linear-gradient(135deg, {cls.COLORS['primary']} 0%, {cls.COLORS['secondary']} 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
            }}
            
            .sub-header {{
                text-align: center;
                color: {cls.COLORS['text_light']};
                font-size: 1.4rem;
                margin-bottom: 2.5rem;
                font-weight: 300;
            }}
            
            .feature-card {{
                background: linear-gradient(135deg, {cls.COLORS['primary']} 0%, {cls.COLORS['accent']} 100%);
                padding: 2rem;
                border-radius: 15px;
                color: white;
                margin-bottom: 1.5rem;
                text-align: center;
                box-shadow: 0 10px 30px rgba(139, 92, 246, 0.2);
                transition: all 0.3s ease;
                border: 1px solid rgba(139, 92, 246, 0.3);
            }}
            
            .feature-card:hover {{
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(139, 92, 246, 0.3);
                border-color: {cls.COLORS['secondary']};
            }}
            
            .welcome-message {{
                background: linear-gradient(135deg, rgba(139,92,246,0.1) 0%, rgba(168,85,247,0.1) 100%);
                padding: 2rem;
                border-radius: 15px;
                margin-bottom: 2.5rem;
                border-left: 4px solid {cls.COLORS['primary']};
                box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                color: {cls.COLORS['text']};
            }}
            
            .metric-card {{
                background: {cls.COLORS['card_bg']};
                padding: 1.8rem;
                border-radius: 12px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.3);
                border-left: 4px solid {cls.COLORS['primary']};
                border: 1px solid {cls.COLORS['border']};
                transition: all 0.3s ease;
                color: {cls.COLORS['text']};
            }}
            
            .metric-card:hover {{
                transform: translateY(-3px);
                box-shadow: 0 12px 35px rgba(0,0,0,0.4);
                border-left-color: {cls.COLORS['secondary']};
            }}
            
            .professional-footer {{
                text-align: center;
                color: {cls.COLORS['text_light']};
                padding: 3rem 0 2rem 0;
                margin-top: 3rem;
                border-top: 2px solid {cls.COLORS['border']};
                background: linear-gradient(135deg, {cls.COLORS['secondary_bg']} 0%, rgba(30, 41, 59, 0.8) 100%);
            }}
            
            .login-form {{
                background: {cls.COLORS['secondary_bg']};
                padding: 3rem;
                border-radius: 20px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.3);
                border: 1px solid {cls.COLORS['border']};
                color: {cls.COLORS['text']};
            }}
            
            /* Dark Theme Form Inputs */
            .stTextInput > div > div > input {{
                background-color: {cls.COLORS['card_bg']};
                color: {cls.COLORS['text']};
                border: 2px solid {cls.COLORS['border']};
                border-radius: 8px;
            }}
            
            .stTextInput > div > div > input:focus {{
                border-color: {cls.COLORS['primary']};
                box-shadow: 0 0 10px rgba(139, 92, 246, 0.3);
            }}
            
            .stSelectbox > div > div > select {{
                background-color: {cls.COLORS['card_bg']};
                color: {cls.COLORS['text']};
                border: 2px solid {cls.COLORS['border']};
            }}
            
            .stNumberInput > div > div > input {{
                background-color: {cls.COLORS['card_bg']};
                color: {cls.COLORS['text']};
                border: 2px solid {cls.COLORS['border']};
            }}
            
            .stTextArea > div > div > textarea {{
                background-color: {cls.COLORS['card_bg']};
                color: {cls.COLORS['text']};
                border: 2px solid {cls.COLORS['border']};
            }}
            
            /* Dark Theme Buttons */
            .stButton > button {{
                background: linear-gradient(135deg, {cls.COLORS['primary']} 0%, {cls.COLORS['accent']} 100%);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 0.8rem 2rem;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 6px 20px rgba(139, 92, 246, 0.3);
            }}
            
            .stButton > button:hover {{
                transform: translateY(-3px);
                box-shadow: 0 10px 30px rgba(139, 92, 246, 0.4);
                background: linear-gradient(135deg, {cls.COLORS['secondary']} 0%, {cls.COLORS['primary']} 100%);
            }}
            
            /* Sidebar Dark Theme */
            .css-1d391kg {{
                background-color: {cls.COLORS['secondary_bg']};
            }}
            
            .sidebar .element-container {{
                margin-bottom: 1rem;
            }}
            
            /* Status Colors */
            .status-success {{
                color: {cls.COLORS['success']};
                font-weight: 600;
            }}
            
            .status-warning {{
                color: {cls.COLORS['warning']};
                font-weight: 600;
            }}
            
            .status-error {{
                color: {cls.COLORS['error']};
                font-weight: 600;
            }}
            
            /* Dark Theme Metrics */
            .metric-value {{
                color: {cls.COLORS['primary']};
                font-weight: bold;
            }}
            
            /* Glow Effects */
            .glow-purple {{
                box-shadow: 0 0 20px rgba(139, 92, 246, 0.4);
            }}
            
            /* Dark scrollbars */
            ::-webkit-scrollbar {{
                width: 8px;
                height: 8px;
            }}
            
            ::-webkit-scrollbar-track {{
                background: {cls.COLORS['secondary_bg']};
            }}
            
            ::-webkit-scrollbar-thumb {{
                background: {cls.COLORS['primary']};
                border-radius: 4px;
            }}
            
            ::-webkit-scrollbar-thumb:hover {{
                background: {cls.COLORS['secondary']};
            }}
        </style>
        """
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate configuration settings."""
        try:
            # Check required directories
            os.makedirs(cls.STORAGE["output_dir"], exist_ok=True)
            
            # Validate AI config
            assert cls.AI_CONFIG["max_questions"] > cls.AI_CONFIG["min_questions"]
            assert cls.AI_CONFIG["default_questions"] <= cls.AI_CONFIG["max_questions"]
            
            # Validate security config
            assert cls.SECURITY["min_password_length"] >= 4
            
            return True
        except Exception as e:
            print(f"Configuration validation failed: {e}")
            return False
