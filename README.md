# 🎓 DSA & Python Tutor Agent

A **Student-Focused DSA Tutor** built with **Google ADK (Agent Development Kit)**, Flask, and Groq/Gemini APIs that teaches Data Structures & Algorithms using a pedagogical, step-by-step approach.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Gemini](https://img.shields.io/badge/LLM-Gemini-purple.svg)
![Groq](https://img.shields.io/badge/LLM-Groq-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Google ADK Framework** - Built using Google's Agent Development Kit
- **Pedagogical Teaching Approach** - Follows an 8-step workflow to teach, not just answer
- **LeetCode-Style Problems** - Designed for interview preparation (Easy → Medium)
- **Python Focused** - All solutions in clean, beginner-friendly Python
- **Dual Backend Support** - Run with Gemini (ADK Web) or Groq (Flask)
- **Custom DSA Tools** - explain_dsa_concept, analyze_complexity, get_leetcode_hints
- **Modern Dark UI** - Beautiful, responsive chat interface
- **Code Highlighting** - Syntax highlighting with copy functionality

## 📸 Screenshots

![DSA Tutor Interface](docs/screenshot.png)

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- [Groq API Key](https://console.groq.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/devanshudhoble/Student-tutor.git
   cd Student-tutor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   # Create .env file
   echo GROQ_API_KEY=your_groq_api_key_here > .env
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Open browser**
   ```
   http://127.0.0.1:5001
   ```

## 🏗️ Project Structure

```
Student-tutor/
├── agent.py                 # 🆕 Google ADK agent entry point
├── agents/
│   ├── __init__.py
│   ├── tutor_agent.py       # Groq-based tutor (Flask backend)
│   └── dsa_tools.py         # 🆕 ADK tools for DSA tutoring
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask app factory
│   └── routes.py            # API endpoints
├── templates/
│   └── index.html           # Modern dark-theme UI
├── tests/
│   └── test_agent.py        # Agent tests
├── .env                     # Environment variables (not in git)
├── .gitignore
├── requirements.txt
├── run.py                   # Flask entry point
└── README.md
```

## 🚀 Two Ways to Run

### Option 1: Google ADK Web UI (Recommended)

```bash
# Set your Google API key
set GOOGLE_API_KEY=your_gemini_api_key

# Run with ADK
adk web
```
Open http://localhost:8000 in your browser.

### Option 2: Flask UI (Groq Backend)

```bash
python run.py
```
Open http://127.0.0.1:5001 in your browser.

| Feature | ADK Web | Flask UI |
|---------|---------|----------|
| Model | Gemini 2.0 Flash | Llama 3.1 (Groq) |
| Tools | ✅ DSA Tools | ❌ |
| UI | ADK Default | Custom Dark Theme |

## 📚 Teaching Workflow

The tutor follows an **8-step pedagogical workflow**:

| Step | Description |
|------|-------------|
| 1️⃣ | **Problem Understanding** - Restate in simple terms |
| 2️⃣ | **Concept Explanation** - Teach the core DSA concept |
| 3️⃣ | **Approach & Logic** - Walk through step-by-step |
| 4️⃣ | **Guided Hints** - Help if student is stuck |
| 5️⃣ | **Python Solution** - Clean, commented code |
| 6️⃣ | **Code Explanation** - Line-by-line breakdown |
| 7️⃣ | **Complexity Analysis** - Time & Space explained |
| 8️⃣ | **Learning Reinforcement** - Similar problems to practice |

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chat interface |
| `/chat` | POST | Send message to tutor |
| `/clear` | POST | Clear conversation history |

### Example Request

```bash
curl -X POST http://127.0.0.1:5001/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain the Two Sum problem"}'
```

## 🤖 Supported Models

The tutor uses Groq's fast inference API with these models:

- `llama-3.1-8b-instant` (Primary)
- `llama-3.3-70b-versatile` (Fallback)
- `qwen/qwen3-32b` (Fallback)

## 📦 Dependencies

```
flask>=3.0.0
python-dotenv>=1.0.0
groq>=0.4.0
```

## 🛠️ Configuration

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | ✅ Yes |
| `MODEL_NAME` | Override default model | ❌ No |
| `FLASK_SECRET_KEY` | Flask session secret | ❌ No |

## 🧪 Testing

```bash
# Run agent test
python -c "import sys; sys.path.insert(0,'.'); from agents.tutor_agent import tutor_agent; print(tutor_agent.handle('explain binary search'))"
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) - Fast LLM inference
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Marked.js](https://marked.js.org/) - Markdown parser
- [Highlight.js](https://highlightjs.org/) - Syntax highlighting

---

<p align="center">
  Made with ❤️ for students preparing for coding interviews
</p>
