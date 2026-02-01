import streamlit as st
from langchain_ollama import OllamaLLM

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
# SETUP
# ----------------------------
st.set_page_config(page_title="MCQ Generator", layout="centered")
create_tables()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------
# LOGIN / SIGNUP
# ----------------------------
if not st.session_state.logged_in:
    st.title("🔐 Login / Signup")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    if col1.button("Login"):
        if login(email, password):
            st.session_state.logged_in = True
            st.session_state.user = email
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    if col2.button("Sign Up"):
        if signup(email, password):
            st.success("Account created. Please login.")
        else:
            st.error("User already exists")

    st.stop()

# ----------------------------
# SIDEBAR – PREVIOUS SESSIONS
# ----------------------------
st.sidebar.title("🕘 Previous MCQ Sessions")

sessions = get_sessions(st.session_state.user)

for session_id, topic, date in sessions:
    if st.sidebar.button(f"{topic} ({date[:10]})", key=f"sess_{session_id}"):
        data = get_session_data(session_id)
        if data:
            topic_loaded, mcq_text = data
            st.session_state.mcqs = mcq_text
            st.success("Loaded previous MCQ session")

# ----------------------------
# MAIN UI
# ----------------------------
st.title("🧠 AI MCQ Generator")
st.write(f"Welcome **{st.session_state.user}**")

topic = st.text_input("Enter Topic")
num_questions = st.number_input("Number of Questions", min_value=1, max_value=20, value=5)
level = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])

# ----------------------------
# GENERATE MCQs
# ----------------------------
if st.button("Generate MCQs"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        llm = OllamaLLM(model="llama3")
        prompt = build_prompt(topic, num_questions, level)

        with st.spinner("Generating MCQs..."):
            response = llm.invoke(prompt)

        st.session_state.mcqs = response
        st.success("MCQs generated successfully!")

# ----------------------------
# SHOW MCQs + SAVE
# ----------------------------
if "mcqs" in st.session_state:
    st.text_area("MCQs", st.session_state.mcqs, height=400)

    if st.button("Save as PDF"):
        pdf_path = save_pdf(st.session_state.mcqs)
        save_history(
            st.session_state.user,
            topic,
            st.session_state.mcqs,
            pdf_path
        )
        st.success(f"Session saved & PDF stored at {pdf_path}")
