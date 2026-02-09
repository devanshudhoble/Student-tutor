"""Minimal working Flask DSA Tutor"""
import os
from pathlib import Path
from flask import Flask, render_template, request, session, jsonify
from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).resolve().parent
app = Flask(
    __name__,
    template_folder=str(base_dir / "templates"),
    static_folder=str(base_dir / "static")
)
app.secret_key = "dev-key"

# Initialize tutor agent safely
tutor_response = None
try:
    from agents.tutor_agent import tutor_agent
    tutor_response = tutor_agent
    print("[OK] Tutor agent loaded")
except Exception as e:
    print(f"[WARN] Tutor agent failed: {e}")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("message", "").strip()
        
        if not msg:
            return jsonify({"response": "Please ask something"}), 200
        
        # Use tutor agent if available
        if tutor_response:
            response = tutor_response.handle(msg)
        else:
            response = f"Echo: {msg}"
        
        return jsonify({"response": response}), 200
    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"response": f"Error: {str(e)}"}), 200

@app.route("/clear", methods=["POST"])
def clear():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)
