#!/usr/bin/env python
"""Simple test server without the tutor agent"""

import os
from pathlib import Path
from flask import Flask, render_template, request, session, jsonify
from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).resolve().parent
templates_dir = str(base_dir / "templates")
static_dir = str(base_dir / "static")

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        
        if not user_message:
            return jsonify({"error": "Empty message"}), 400
        
        # Simple mock response
        response = f"Echo: {user_message}\n\nThis is a test response."
        
        return jsonify({"response": response})
    
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/clear", methods=["POST"])
def clear_chat():
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    print("Starting test app on http://127.0.0.1:5001")
    app.run(host="127.0.0.1", port=5001, debug=False)
