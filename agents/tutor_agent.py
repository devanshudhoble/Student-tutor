import os
import time
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini (NEW SDK)
try:
    from groq import Groq

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set")
    client = Groq(api_key=api_key)
    print("[DEBUG] Groq client initialized successfully")
except Exception as e:
    print(f"[WARNING] Failed to initialize Groq: {e}")
    client = None


def list_models():
    """Return a list of available model IDs from the Gemini client (best-effort)."""
    if not client:
        return {"error": "client not initialized"}

    # Try several possible list methods depending on SDK version
    try:
        # Preferred: client.models.list()
        if hasattr(client, 'models') and hasattr(client.models, 'list'):
            resp = client.models.list()
            # try to extract model ids
            models = []
            for m in getattr(resp, 'models', []) or []:
                mid = getattr(m, 'name', None) or getattr(m, 'id', None) or str(m)
                if mid:
                    models.append(mid)
            return {"models": models}

        # Fallback: client.list_models()
        if hasattr(client, 'list_models'):
            resp = client.list_models()
            models = [getattr(m, 'name', getattr(m, 'id', str(m))) for m in (resp or [])]
            return {"models": models}

        # Last resort: call list via raw API
        return {"error": "no supported list method on client"}
    except Exception as e:
        return {"error": str(e)}

SYSTEM_PROMPT = """
You are a Student-Focused DSA Tutor Agent built using the Google ADK Agent Framework.

ROLE:
You act as an interactive Python DSA tutor specifically designed to help students solve LeetCode-style problems.
Your goal is to teach, not just answer.

You are NOT a generic ChatGPT-style assistant.
You must strictly follow a pedagogical, student-first workflow.

PLATFORM CONTEXT:
- Backend: Flask-based web application
- Agent Framework: Google ADK
- User: A student learning Data Structures & Algorithms using Python
- Problem Source Style: LeetCode-level problems (Easy → Medium)

PRIMARY OBJECTIVE:
Guide the student step-by-step to understand and solve a given DSA problem using Python.

--------------------------------------------------
AGENT WORKFLOW (MANDATORY & SEQUENTIAL)
--------------------------------------------------

STEP 1: PROBLEM UNDERSTANDING
- Assume the problem is similar to a LeetCode DSA question.
- Restate the problem in very simple, student-friendly language.
- Clearly explain:
  - What is given
  - What is expected as output
  - Any constraints (time/space, input size)
- Do NOT give code in this step.

STEP 2: CONCEPT EXPLANATION
- Identify the core DSA concept involved (e.g., Array, Hashing, Two Pointers, Stack, Recursion, Binary Search, etc.).
- Explain the concept from scratch as if teaching a beginner.
- Use simple analogies or real-world examples.
- Avoid heavy jargon.
- Use short paragraphs or bullet points.

STEP 3: APPROACH & LOGIC
- Explain how the concept applies to THIS problem.
- Walk through the logic step-by-step.
- Include a dry run with a small example input.
- Do NOT give full code yet.
- Mention if the student should try solving it themselves first.

STEP 4: GUIDED HINTS (IF STUDENT IS STUCK)
- If the student is unable to solve:
  - Provide hints, not the solution immediately.
  - Gradually increase hint clarity.
  - Still avoid full code unless necessary.

STEP 5: PYTHON SOLUTION (ONLY AFTER EXPLANATION)
- Provide a clean, readable Python solution.
- Use beginner-friendly syntax.
- Add inline comments for every logical step.
- Follow LeetCode-style function format.

STEP 6: CODE EXPLANATION
- Explain the provided Python code line-by-line.
- Emphasize:
  - Why each step exists
  - How time complexity is achieved
  - Space complexity in simple terms

STEP 7: COMPLEXITY ANALYSIS
- Clearly state:
  - Time Complexity
  - Space Complexity
- Explain what they mean in simple language.

STEP 8: LEARNING REINFORCEMENT
- Suggest:
  - 1–2 similar LeetCode problems to practice
  - A small practice variation
- Encourage the student.

--------------------------------------------------
STRICT RULES
--------------------------------------------------
- Be student-friendly and encouraging.
- Never overwhelm with advanced theory.
- Prefer clarity over brevity.
- Avoid unnecessary optimizations unless required.
- Never jump directly to code without explanation.
- Assume the student is learning DSA for placements/interviews.

--------------------------------------------------
OUTPUT STYLE
--------------------------------------------------
- Use clear headings (###, ####)
- Simple, plain English
- Short paragraphs
- Python-focused
- Teaching tone, not expert arrogance
- Markdown formatting for readability

--------------------------------------------------
FAILURE HANDLING
--------------------------------------------------
If a student is confused:
- Re-explain using a different example
- Slow down
- Use even simpler language

--------------------------------------------------
END GOAL
--------------------------------------------------
By the end of the interaction, the student should:
- Understand the DSA concept
- Understand how to approach similar problems
- Be confident solving LeetCode problems independently

You are a TUTOR, not just a code generator.
"""

class DSATutorAgent:
    def __init__(self):
        self.name = "DSA_Tutor_Agent"
        self.description = "Student-Focused DSA & Python Tutor using Groq"

    def handle(self, user_message: str, context: str = "") -> str:
        """
        Handle student question/problem using pedagogical workflow with retry logic.
        Uses Groq API (chat.completions format).
        """
        if not client:
            return "⚠️ AI service not available. Please try again later."
        
        try:
            full_prompt = f"""{SYSTEM_PROMPT}

{context if context else ''}

STUDENT QUESTION/PROBLEM:
{user_message}

Provide a comprehensive, pedagogical response following the 8-step workflow above.
Use markdown formatting with clear headings.
Remember: You are a TUTOR, not a code generator.
"""

            # Retry logic: attempt up to 3 rounds; try multiple candidate models (env override + Groq models)
            last_exc = None
            env_model = os.getenv("MODEL_NAME")
            # Candidate list: env override first, then Groq model names
            candidates = []
            if env_model:
                candidates.append(env_model)
            candidates.extend([m for m in ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "qwen/qwen3-32b"] if m not in candidates])

            for attempt in range(1, 4):
                for model_name in candidates:
                    try:
                        print(f"[DEBUG] Attempt {attempt}/3 — trying model '{model_name}'")
                        response = client.chat.completions.create(
                            model=model_name,
                            messages=[
                                {"role": "user", "content": full_prompt}
                            ],
                            temperature=0.7,
                            max_tokens=2048
                        )

                        print(f"[DEBUG] Response received type: {type(response)}")
                        if response and response.choices and len(response.choices) > 0:
                            content = response.choices[0].message.content
                            if content:
                                print(f"[DEBUG] Success with model '{model_name}' on attempt {attempt}")
                                return content

                        last_exc = RuntimeError(f"Empty or invalid response from API (model={model_name}, attempt={attempt})")
                        print(f"[DEBUG] {last_exc}")
                    except Exception as e:
                        print(f"[DEBUG] Exception with model '{model_name}' on attempt {attempt}: {type(e).__name__}: {e}")
                        last_exc = e
                        # continue to next candidate
                if attempt < 3:
                    wait_time = 0.5 * attempt
                    print(f"[DEBUG] Waiting {wait_time}s before next round...")
                    time.sleep(wait_time)

            # Graceful fallback if all retries fail
            print(f"[ERROR] Groq API failed after retries: {last_exc}")
            fallback = "### 🤖 Tutor Response\n\n"
            fallback += "I'm having temporary trouble reaching the AI model, but I can still help!\n\n"
            fallback += "**Problem Summary:**\n"
            fallback += (user_message[:200] + '...' if len(user_message) > 200 else user_message) + "\n\n"
            fallback += "**General Approach:**\n"
            fallback += "1. **Understand**: Break down what input you have and what output is needed.\n"
            fallback += "2. **Identify DSA Concept**: Think about arrays, hashing, two-pointers, recursion, or dynamic programming.\n"
            fallback += "3. **Design**: Work through a small example by hand.\n"
            fallback += "4. **Code**: Write clean Python code with comments.\n"
            fallback += "5. **Analyze**: Calculate time and space complexity.\n\n"
            fallback += "**Try Again**: Send your question again and I'll attempt a full AI-powered response!"
            return fallback

        except Exception as e:
            print(f"[ERROR] Unexpected error in handle(): {e}")
            return f"❌ Unexpected error: {str(e)}\n\nPlease refresh and try again."


# Agent instance
tutor_agent = DSATutorAgent()



