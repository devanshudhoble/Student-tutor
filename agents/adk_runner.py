"""
ADK Agent Runner for Flask Integration

This module provides a wrapper to run the Google ADK agent programmatically
from Flask routes instead of using `adk web`.
"""

import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Ensure Google API key is set
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import root_agent

# Create session service for conversation memory
session_service = InMemorySessionService()

# Create runner with the ADK agent
runner = Runner(
    agent=root_agent,
    app_name="dsa_tutor_flask",
    session_service=session_service,
)

# Track created sessions
_created_sessions = set()


async def _ensure_session_exists(user_id: str, session_id: str):
    """Ensure a session exists, creating it if necessary."""
    session_key = f"{user_id}:{session_id}"
    if session_key not in _created_sessions:
        try:
            # Try to get existing session
            existing = await session_service.get_session(
                app_name="dsa_tutor_flask",
                user_id=user_id,
                session_id=session_id
            )
            if existing:
                _created_sessions.add(session_key)
                return
        except:
            pass
        
        # Create new session
        await session_service.create_session(
            app_name="dsa_tutor_flask",
            user_id=user_id,
            session_id=session_id
        )
        _created_sessions.add(session_key)
        print(f"[DEBUG] Created session: {session_id}")


async def _run_agent_async(user_message: str, session_id: str = "default_session") -> str:
    """
    Run the ADK agent asynchronously and return the response.
    """
    user_id = "flask_user"
    
    try:
        # Ensure session exists
        await _ensure_session_exists(user_id, session_id)
        
        # Create content from user message
        content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_message)]
        )
        
        # Run the agent and collect response
        response_parts = []
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=content
        ):
            # Extract text from agent response events
            if hasattr(event, 'content') and event.content:
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        response_parts.append(part.text)
        
        if response_parts:
            return "".join(response_parts)
        else:
            return "I'm processing your request. Please try again."
            
    except Exception as e:
        print(f"[ERROR] ADK Runner error: {e}")
        import traceback
        traceback.print_exc()
        raise


def run_adk_agent(user_message: str, session_id: str = "default_session") -> str:
    """
    Synchronous wrapper to run the ADK agent from Flask.
    
    Args:
        user_message: The user's question or problem
        session_id: Session ID for conversation continuity
    
    Returns:
        The agent's response as a string
    """
    try:
        # Get or create event loop
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If loop is already running, use thread
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(asyncio.run, _run_agent_async(user_message, session_id))
                    return future.result(timeout=120)
            else:
                return loop.run_until_complete(_run_agent_async(user_message, session_id))
        except RuntimeError:
            # No event loop exists, create one
            return asyncio.run(_run_agent_async(user_message, session_id))
            
    except Exception as e:
        print(f"[ERROR] run_adk_agent error: {e}")
        return f"❌ Error calling AI agent: {str(e)}"


# Test function
if __name__ == "__main__":
    print("Testing ADK agent...")
    response = run_adk_agent("Explain the two sum problem briefly")
    print("Response:", response[:500] if len(response) > 500 else response)
