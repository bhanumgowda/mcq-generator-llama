import sqlite3
import hashlib

def get_db():
    return sqlite3.connect("users.db")

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
    except:
        return False
    finally:
        conn.close()

def login(email, password):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )
    user = c.fetchone()
    conn.close()
    return user is not None

def save_history(email, topic, pdf_path):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO history (email, topic, pdf_path) VALUES (?, ?, ?)",
        (email, topic, pdf_path)
    )
    conn.commit()
    conn.close()

def get_history(email):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT topic, pdf_path, created_at FROM history WHERE email=? ORDER BY created_at DESC",
        (email,)
    )
    rows = c.fetchall()
    conn.close()
    return rows






