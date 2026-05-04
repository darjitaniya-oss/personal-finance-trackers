import sqlite3

def connect():
    conn = sqlite3.connect("data.db")
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        type TEXT,
        amount REAL
    )
    """)

    conn.commit()
    conn.close()
