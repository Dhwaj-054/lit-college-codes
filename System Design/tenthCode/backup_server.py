from flask import Flask, request, jsonify, redirect
from db import init_db, insert_url, get_url
import string
import random

app = Flask(__name__)
init_db()


@app.route('/')
def home():
    return jsonify({
        "service": "URL Shortener API Backup",
        "status": "running",
        "endpoints": ["POST /shorten", "GET /go/<short_code>"]
    })

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.json
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL required"}), 400

    short_code = generate_short_code()
    insert_url(short_code, original_url)

    return jsonify({
        "short_url": f"http://localhost:5001/go/{short_code}"
    })


@app.route('/go/<short_code>')
def redirect_url(short_code):
    original_url = get_url(short_code)

    if original_url:
        return redirect(original_url)
    else:
        return jsonify({"error": "URL not found"}), 404


if __name__ == '__main__':
    print("Backup API running on http://localhost:5001")
    app.run(port=5001)
