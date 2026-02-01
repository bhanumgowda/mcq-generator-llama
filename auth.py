import sqlite3
import hashlib

DB_NAME = "users.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        topic TEXT,
        mcq_text TEXT,
        pdf_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(email, password):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, hash_password(password))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login(email, password):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT id FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )
    row = c.fetchone()
    conn.close()
    return row is not None

def save_history(email, topic, mcq_text, pdf_path):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO history (email, topic, mcq_text, pdf_path) VALUES (?, ?, ?, ?)",
        (email, topic, mcq_text, pdf_path)
    )
    conn.commit()
    conn.close()

def get_sessions(email):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT id, topic, created_at FROM history WHERE email=? ORDER BY created_at DESC",
        (email,)
    )
    rows = c.fetchall()
    conn.close()
    return rows

def get_session_data(session_id):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT topic, mcq_text FROM history WHERE id=?",
        (session_id,)
    )
    row = c.fetchone()
    conn.close()
    return row






