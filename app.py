import streamlit as st
from langchain_ollama import OllamaLLM
import time

from config import Config
from prompt import build_prompt
from pdf_generator import save_pdf
from auth import (
    create_tables,
    signup,
    login,
    save_history,
    get_sessions,
    get_session_data
)

# ----------------------------
# PAGE CONFIG & PROFESSIONAL SETUP
# ----------------------------
st.set_page_config(**Config.UI_CONFIG)

# Validate configuration
if not Config.validate_config():
    st.error("❌ Configuration validation failed. Please check your setup.")
    st.stop()

# Apply professional styling
st.markdown(Config.get_css_styles(), unsafe_allow_html=True)

create_tables()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------
# PROFESSIONAL LOGIN / SIGNUP PAGE
# ----------------------------
if not st.session_state.logged_in:
    # Professional header
    st.markdown(f'<h1 class="main-header">🎓 {Config.APP_NAME}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">{Config.APP_DESCRIPTION}</p>', unsafe_allow_html=True)
    
    # Feature showcase
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🧠 AI-Powered</h3>
            <p>Advanced AI generates high-quality questions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📚 Multi-Level</h3>
            <p>Easy to Hard difficulty levels</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📄 PDF Export</h3>
            <p>Professional PDF generation</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Professional login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🔐 Access Your Account")
        
        with st.form("login_form"):
            email = st.text_input("📧 Email Address", placeholder="Enter your email")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
            
            col_login, col_signup = st.columns(2)
            
            login_clicked = col_login.form_submit_button("🚀 Login", use_container_width=True)
            signup_clicked = col_signup.form_submit_button("📝 Sign Up", use_container_width=True)
            
            if login_clicked:
                if not email or not password:
                    st.error("⚠️ Please fill in all fields")
                elif login(email, password):
                    st.session_state.logged_in = True
                    st.session_state.user = email
                    st.success(Config.MESSAGES["login_success"])
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(Config.MESSAGES["login_error"])
            
            if signup_clicked:
                if not email or not password:
                    st.error("⚠️ Please fill in all fields")
                elif len(password) < Config.SECURITY["min_password_length"]:
                    st.error(f"⚠️ Password must be at least {Config.SECURITY['min_password_length']} characters long")
                elif signup(email, password):
                    st.success(Config.MESSAGES["signup_success"])
                else:
                    st.error(Config.MESSAGES["signup_error"])

    # Professional footer for login page
    st.markdown(f"""
    <div class="professional-footer">
        <p><strong>{Config.APP_NAME} v{Config.APP_VERSION}</strong> - Revolutionizing education through AI</p>
        <p><small>© 2026 {Config.APP_NAME}. All rights reserved.</small></p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# ----------------------------
# SIDEBAR – DASHBOARD & HISTORY
# ----------------------------
with st.sidebar:
    st.markdown("### 👤 User Dashboard")
    st.markdown(f"**Logged in as:** {st.session_state.user}")
    
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.clear()
        st.rerun()
    
    st.markdown("---")
    
    # Statistics
    sessions = get_sessions(st.session_state.user)
    st.markdown("### 📊 Your Stats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Sessions", len(sessions))
    with col2:
        # Calculate total questions (assuming 5 per session on average)
        total_questions = len(sessions) * 5
        st.metric("Questions Created", f"{total_questions}+")
    
    st.markdown("---")
    
    # Previous sessions
    st.markdown("### 📚 Previous Sessions")
    
    if not sessions:
        st.info("No previous sessions found. Create your first MCQ set!")
    else:
        for session_id, topic, date in sessions:
            with st.container():
                # Format date nicely
                formatted_date = date[:10]
                if st.button(
                    f"📖 {topic}", 
                    key=f"sess_{session_id}",
                    help=f"Created on {formatted_date}",
                    use_container_width=True
                ):
                    data = get_session_data(session_id)
                    if data:
                        topic_loaded, mcq_text = data
                        st.session_state.mcqs = mcq_text
                        st.session_state.loaded_topic = topic_loaded
                        st.success(f"✅ Loaded: {topic_loaded}")
                        st.rerun()

# ----------------------------
# MAIN APPLICATION INTERFACE
# ----------------------------
st.markdown('<h1 class="main-header">🎓 EduQuiz Pro</h1>', unsafe_allow_html=True)

# Welcome message
st.markdown(f"""
<div class="welcome-message">
    <h3>👋 Welcome back, <strong>{st.session_state.user.split('@')[0].title()}</strong>!</h3>
    <p>Ready to create some amazing MCQs? Let's get started!</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# PROFESSIONAL MCQ GENERATION FORM
# ----------------------------
st.markdown("### 🎯 Create Your MCQ Set")

with st.form("mcq_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        topic = st.text_input(
            "📚 Topic/Subject", 
            placeholder="e.g., Python Programming, World History, Biology...",
            help="Enter the topic you want to create MCQs for"
        )
        
        num_questions = st.number_input(
            "📊 Number of Questions", 
            min_value=Config.AI_CONFIG["min_questions"], 
            max_value=Config.AI_CONFIG["max_questions"], 
            value=Config.AI_CONFIG["default_questions"],
            help=f"Choose between {Config.AI_CONFIG['min_questions']} and {Config.AI_CONFIG['max_questions']} questions"
        )
    
    with col2:
        level = st.selectbox(
            "⚡ Difficulty Level", 
            Config.AI_CONFIG["difficulty_levels"],
            help="Select the difficulty level for your questions"
        )
        
        st.markdown("#### 💡 Professional Tips:")
        st.markdown("""
        - Be specific with your topic for better results
        - Start with fewer questions (5-10) for testing
        - Easy: Basic concepts and definitions
        - Medium: Applied knowledge and problem-solving  
        - Hard: Complex analysis and evaluation
        """)
    
    # Professional generate button
    submitted = st.form_submit_button("🚀 Generate MCQs", use_container_width=True, type="primary")
    
    if submitted:
        if not topic.strip():
            st.error("⚠️ Please enter a topic before generating MCQs")
        else:
            with st.spinner("🤖 AI is crafting your questions... This may take a moment"):
                try:
                    llm = OllamaLLM(model=Config.AI_CONFIG["model_name"])
                    prompt = build_prompt(topic, num_questions, level)
                    
                    # Professional progress indication
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for i in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(i + 1)
                        if i < 30:
                            status_text.text("🧠 AI analyzing your topic...")
                        elif i < 60:
                            status_text.text("📝 Generating questions...")
                        elif i < 90:
                            status_text.text("🎯 Crafting answer options...")
                        else:
                            status_text.text("✨ Finalizing your MCQ set...")
                    
                    response = llm.invoke(prompt)
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    st.session_state.mcqs = response
                    st.session_state.current_topic = topic
                    st.session_state.current_level = level
                    st.session_state.current_num = num_questions
                    
                    st.success(Config.MESSAGES["mcq_success"])
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Error generating MCQs: {str(e)}")
                    st.info("💡 Make sure Ollama is running and the llama3 model is installed")
                    if "Connection" in str(e):
                        st.warning("🔗 Check if Ollama service is running: `ollama serve`")

# ----------------------------
# DISPLAY & MANAGE MCQs
# ----------------------------
if "mcqs" in st.session_state and st.session_state.mcqs:
    st.markdown("---")
    st.markdown("### 📝 Generated MCQs")
    
    # Display metadata if available
    if "current_topic" in st.session_state:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"**📚 Topic:** {st.session_state.get('current_topic', 'Loaded from history')}")
        with col2:
            st.markdown(f"**⚡ Level:** {st.session_state.get('current_level', 'N/A')}")
        with col3:
            st.markdown(f"**📊 Questions:** {st.session_state.get('current_num', 'N/A')}")
        with col4:
            if "loaded_topic" in st.session_state:
                st.markdown("**🔄 Status:** Loaded from history")
            else:
                st.markdown("**✨ Status:** Newly generated")
    
    # Display MCQs in a nice container
    st.markdown("#### Your MCQ Set:")
    st.text_area(
        "MCQs", 
        st.session_state.mcqs, 
        height=500,
        help="Your generated MCQs are displayed here. You can copy this text or save as PDF.",
        key="mcq_display"
    )
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Save as PDF", use_container_width=True, type="primary"):
            try:
                with st.spinner("📄 Creating PDF..."):
                    topic_to_save = st.session_state.get('current_topic', st.session_state.get('loaded_topic', 'Untitled'))
                    pdf_path = save_pdf(
                        st.session_state.mcqs, 
                        topic=topic_to_save,
                        user_email=st.session_state.user
                    )
                    
                    # Save to history
                    save_history(
                        st.session_state.user,
                        topic_to_save,
                        st.session_state.mcqs,
                        pdf_path
                    )
                    
                    st.success(f"✅ PDF saved successfully!")
                    st.info(f"📍 Location: {pdf_path}")
                    
            except Exception as e:
                st.error(f"❌ Error saving PDF: {str(e)}")
    
    with col2:
        if st.button("🔄 Generate New Set", use_container_width=True):
            # Clear current MCQs to force new generation
            if "mcqs" in st.session_state:
                del st.session_state.mcqs
            if "current_topic" in st.session_state:
                del st.session_state.current_topic
            if "loaded_topic" in st.session_state:
                del st.session_state.loaded_topic
            st.rerun()
    
    with col3:
        # Copy to clipboard button (using a workaround)
        st.markdown(f"""
        <button onclick="navigator.clipboard.writeText(`{st.session_state.mcqs.replace('`', '\\`')}`)">
            📋 Copy to Clipboard
        </button>
        """, unsafe_allow_html=True)

# ----------------------------
# PROFESSIONAL FOOTER
# ----------------------------
st.markdown("---")
st.markdown(f"""
<div class="professional-footer">
    <p>🎓 <strong>{Config.APP_NAME} v{Config.APP_VERSION}</strong> - Powered by AI | Made with ❤️ using Streamlit</p>
    <p><small>© 2026 {Config.APP_NAME}. Revolutionizing education through AI.</small></p>
    <p><small>Built with Streamlit • Powered by Ollama • Enhanced with ReportLab</small></p>
</div>
""", unsafe_allow_html=True)