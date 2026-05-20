import sqlite3

DB_NAME = "url_shortener.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        short_code TEXT PRIMARY KEY,
        original_url TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_url(short_code, original_url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO urls VALUES (?, ?)", (short_code, original_url))

    conn.commit()
    conn.close()


def get_url(short_code):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT original_url FROM urls WHERE short_code=?", (short_code,))
    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None