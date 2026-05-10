from flask import Flask, request, redirect, render_template_string, url_for
import sqlite3
import string
import random
from urllib.parse import urlparse

app = Flask(__name__)
DB_FILE = "shortener.db"

HTML = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Local URL Shortener</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; line-height: 1.5; }
        input[type=text] { width: 100%; padding: 10px; margin: 8px 0; }
        button { padding: 10px 16px; cursor: pointer; }
        .box { background: #f7f7f7; padding: 16px; border-radius: 8px; margin-top: 14px; }
        .error { color: #b00020; }
    </style>
</head>
<body>
    <h2>URL Shortener (Local)</h2>
    <form method="post" action="/shorten">
        <label>Enter URL:</label>
        <input type="text" name="long_url" placeholder="https://example.com/page" required>
        <button type="submit">Shorten</button>
    </form>

    {% if error %}
      <p class="error">{{ error }}</p>
    {% endif %}

    {% if short_url %}
      <div class="box">
        <b>Short URL:</b><br>
        <a href="{{ short_url }}" target="_blank">{{ short_url }}</a>
      </div>
    {% endif %}
</body>
</html>
"""

def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                long_url TEXT NOT NULL
            )
        """)
        conn.commit()

def valid_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def unique_code():
    while True:
        code = generate_code()
        with get_conn() as conn:
            row = conn.execute("SELECT 1 FROM urls WHERE code = ?", (code,)).fetchone()
            if not row:
                return code

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.form.get("long_url", "").strip()

    if not valid_url(long_url):
        return render_template_string(HTML, error="Please enter a valid URL starting with http:// or https://")

    code = unique_code()
    with get_conn() as conn:
        conn.execute("INSERT INTO urls (code, long_url) VALUES (?, ?)", (code, long_url))
        conn.commit()

    short_url = url_for("go", code=code, _external=True)
    return render_template_string(HTML, short_url=short_url)

@app.route("/<code>", methods=["GET"])
def go(code):
    with get_conn() as conn:
        row = conn.execute("SELECT long_url FROM urls WHERE code = ?", (code,)).fetchone()

    if row:
        return redirect(row["long_url"])
    return "Short URL not found.", 404

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
