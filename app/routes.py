"""
Flask Routes for DSA Tutor
Uses Groq-based tutor agent with Google ADK framework structure.
"""

from flask import Blueprint, render_template, request, session, jsonify
from agents.tutor_agent import tutor_agent
import json

main_routes = Blueprint("main_routes", __name__)


@main_routes.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main_routes.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        
        if not user_message:
            return jsonify({"error": "Empty message"}), 400
        
        # Get conversation history from session
        chat_history = session.get("chat_history", [])
        
        # Build context from chat history (keep last 4 messages for context)
        context = ""
        if chat_history and len(chat_history) > 0:
            context = "\n\n--- PREVIOUS CONVERSATION CONTEXT ---\n"
            for msg in chat_history[-4:]:
                context += f"Student: {msg['user'][:150]}...\n"
                context += f"Tutor: {msg['tutor'][:200]}...\n\n"
            context += "--- END CONTEXT ---\n"
        
        # Get response from tutor agent with context
        response = tutor_agent.handle(user_message, context)
        
        # Store in chat history
        chat_history.append({
            "user": user_message,
            "tutor": response
        })
        session["chat_history"] = chat_history
        
        return jsonify({
            "response": response,
            "history_length": len(chat_history),
            "backend": "Groq/Llama"
        })
    
    except Exception as e:
        print(f"[ERROR] Chat endpoint error: {str(e)}")
        return jsonify({
            "error": f"Server error: {str(e)}",
            "response": "❌ Sorry, I encountered a server error. Please try again or refresh the page."
        }), 500


@main_routes.route("/clear", methods=["POST"])
def clear_chat():
    try:
        session.pop("chat_history", None)
        return jsonify({"status": "cleared"})
    except Exception as e:
        print(f"[ERROR] Clear endpoint error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@main_routes.route("/status", methods=["GET"])
def status():
    """Check backend status."""
    return jsonify({
        "backend": "Groq/Llama",
        "framework": "Google ADK (structure)",
        "status": "ok"
    })
