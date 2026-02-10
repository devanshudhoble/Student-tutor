# 🎓 ADK Python DSA Tutor — Web App

A **Student-Focused DSA & Python Tutor** web application built with **Google ADK (Agent Development Kit)** and **Flask**. It uses a pedagogical, step-by-step workflow to teach Data Structures & Algorithms through an interactive chat interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![Google ADK](https://img.shields.io/badge/Google%20ADK-Agent%20Framework-orange)
![Groq](https://img.shields.io/badge/Groq-LLM%20Backend-green)

---

## ✨ Features

- 🤖 **AI-Powered Tutoring** — Follows an 8-step pedagogical workflow (understand → explain → approach → hints → solution → explain code → complexity → practice)
- 🧠 **Google ADK Integration** — Uses ADK Agent framework with custom DSA tools
- 💬 **Modern Chat UI** — Dark-themed, responsive Flask web interface with markdown & code highlighting
- 🔧 **Custom DSA Tools** — `explain_dsa_concept`, `analyze_complexity`, `get_leetcode_hints`
- ⚡ **Groq LLM Backend** — Fast inference with Groq API (Llama models)
- 🔄 **Dual Mode** — Run via Flask UI or `adk web` interface

---

## 🏗️ Architecture

```
ADK-python-tutor-web-app/
├── agent.py                  # Google ADK agent definition (Gemini)
├── run.py                    # Flask web server (Groq backend)
├── agents/
│   ├── __init__.py           # Package exports
│   ├── tutor_agent.py        # Groq-powered DSA tutor agent
│   ├── dsa_tools.py          # Custom ADK tools for DSA concepts
│   └── adk_runner.py         # ADK-to-Flask bridge runner
├── templates/
│   └── index.html            # Chat UI (dark theme)
├── requirements.txt          # Python dependencies
└── .env                      # API keys (not tracked)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Groq API Key → [Get one here](https://console.groq.com)
- Google API Key (optional, for ADK/Gemini mode) → [Get one here](https://aistudio.google.com/apikey)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/devanshudhoble/ADK-python-tutor-web-app.git
cd ADK-python-tutor-web-app

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo GROQ_API_KEY=your_groq_api_key_here > .env
echo GOOGLE_API_KEY=your_google_api_key_here >> .env
```

### Run the App

#### Option 1: Flask Web App (Recommended)

```bash
python run.py
```

Open **http://127.0.0.1:5001** in your browser.

#### Option 2: ADK Web Interface

```bash
adk web
```

Open **http://127.0.0.1:8000** in your browser.

---

## 🛠️ Custom ADK Tools

| Tool | Description |
|------|-------------|
| `explain_dsa_concept(concept)` | Explains DSA concepts (arrays, trees, graphs, DP, etc.) in beginner-friendly language |
| `analyze_complexity(code_description)` | Analyzes time & space complexity with a reference table |
| `get_leetcode_hints(problem_name, hint_level)` | Progressive hints (level 1–3) for LeetCode problems without spoiling the solution |

---

## 🧑‍🏫 How the Tutor Works

The agent follows a **mandatory 8-step pedagogical workflow**:

1. **Problem Understanding** — Restates the problem in simple language
2. **Concept Explanation** — Teaches the core DSA concept with analogies
3. **Approach & Logic** — Walks through the solution logic with a dry run
4. **Guided Hints** — Provides progressive hints if the student is stuck
5. **Python Solution** — Clean, commented Python code (LeetCode-style)
6. **Code Explanation** — Line-by-line code walkthrough
7. **Complexity Analysis** — Time & space complexity in plain English
8. **Learning Reinforcement** — Suggests similar problems for practice

---

## 📸 Screenshot

The web app features a modern dark-themed chat interface:

- Clean header with app title
- Quick-access topic buttons (Two Sum, Linked Lists, Binary Search, DP)
- Chat area with user/bot avatars and markdown rendering
- Syntax-highlighted code blocks with copy button

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | ✅ Yes | Groq API key for LLM inference |
| `GOOGLE_API_KEY` | Optional | Google API key for ADK/Gemini mode |
| `GEMINI_API_KEY` | Optional | Alternative Gemini key |

---

## 📦 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Flask (Python)
- **Agent Framework**: Google ADK
- **LLM**: Groq (Llama 3.1 / 3.3)
- **Libraries**: marked.js (Markdown), highlight.js (Syntax highlighting)

---

## 📄 License

This project is for educational purposes.

---

## 👤 Author

**Devanshu Dhoble**

- GitHub: [@devanshudhoble](https://github.com/devanshudhoble)
