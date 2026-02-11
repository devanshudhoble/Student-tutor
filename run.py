"""
Flask DSA Tutor with Google ADK Integration

This application uses Flask as the frontend web framework and integrates
Google ADK Agent tools with Groq LLM as the backend model.
"""
import os
import uuid
from pathlib import Path
from flask import Flask, render_template, request, session, jsonify
from dotenv import load_dotenv

load_dotenv()

# --- Google ADK Framework (loaded lazily to avoid slow startup) ---
# ADK Agent is defined in agent.py and can be run via `adk web`
# For Flask, we use the lightweight DSA tools directly
from agents.dsa_tools import explain_dsa_concept, analyze_complexity, get_leetcode_hints

# --- Flask App Setup ---
base_dir = Path(__file__).resolve().parent
app = Flask(
    __name__,
    template_folder=str(base_dir / "templates"),
    static_folder=str(base_dir / "static")
)
app.secret_key = "dev-key"

# --- Initialize Groq-powered Tutor Agent ---
tutor = None
try:
    from agents.tutor_agent import tutor_agent
    tutor = tutor_agent
    print("[OK] DSA Tutor Agent loaded (Groq backend)")
except Exception as e:
    print(f"[WARN] Tutor agent failed to load: {e}")


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

        # Use Groq-powered tutor agent
        if tutor:
            response = tutor.handle(msg)
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
    print("\n=== DSA Tutor Flask App ===")
    print("Framework: Google ADK + Flask")
    print("Model: Groq LLM")
    print("Tools: explain_dsa_concept, analyze_complexity, get_leetcode_hints")
    print("URL: http://127.0.0.1:5001\n")
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)

