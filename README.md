🎓 AI Personalized Tutor — Real-Time Voice Learning Assistant

An interactive AI-powered learning assistant that allows users to ask questions via text or voice and receive step-by-step explanations with voice output.

Built with a modular FastAPI backend and a clean Streamlit frontend, powered by Meta LLaMA-3 (via OpenRouter API).

💬 Speak or type your question — the tutor listens, understands context, and responds intelligently.

🧠 Features

🎙️ Voice Input — Ask questions naturally using your microphone
⌨️ Text Input — Type queries directly into the UI
🔊 Voice Output (TTS) — AI responses are spoken aloud
🧠 Context Memory — Maintains last 10 messages for multi-turn interaction
🔐 Secure API Handling — API keys stored safely in .env
⚡ Lightweight — Runs on CPU, no GPU required
🖥️ Interactive UI — Clean and simple Streamlit interface
🏗️ Modular Architecture — Separate frontend and backend for scalability

🏗️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend	FastAPI
LLM	Meta LLaMA-3 (via OpenRouter API)
Speech Input	Google SpeechRecognition
Speech Output	pyttsx3 (Windows SAPI5)
HTTP Client	Requests
Environment Config	python-dotenv

📁 Project Structure
AI-Personalized-Tutor/
│
├── backend/
│   ├── main.py        # FastAPI app + API routes
│   ├── model.py       # LLaMA-3 integration logic
│   ├── config.py      # Environment variable handling
    ├── tts.py         # For output Voice 
│   └── __init__.py
│
├── frontend/
│   ├── app.py         # Streamlit UI + Speech Recognition
│   └── tts.py         # Text-to-Speech service
│
├── .env               # OPENROUTER_API_KEY stored here
├── requirements.txt   # Dependencies
└── README.md          # Project documentation


Clean separation between frontend and backend ensures modularity and scalability.

🧠 System Architecture
User (Voice / Text)
        ↓
Streamlit Frontend
        ↓
Google SpeechRecognition (if voice)
        ↓
FastAPI Backend
        ↓
OpenRouter API → LLaMA-3
        ↓
AI Response
        ↓
pyttsx3 (Text-to-Speech)
        ↓
Spoken Output to User


The system follows a client–server architecture, ensuring secure API key management and clean separation of concerns.

🧰 Installation Guide
1️⃣ Create Virtual Environment
python -m venv mvenv
mvenv\Scripts\activate   # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Setup

Create a .env file in the root directory:

OPENROUTER_API_KEY=your_openrouter_api_key_here


Get your API key from:
👉 https://openrouter.ai

🚀 Run the Application
Step 1: Start Backend
uvicorn backend.main:app --reload


Backend runs at:

http://127.0.0.1:8000

Step 2: Start Frontend
streamlit run frontend/app.py


Open in browser:

http://localhost:8501

🗣️ Sample Questions to Try

“Explain stacks in data structures.”

“What is machine learning in simple words?”

“How does binary search work?”

“What is overfitting?”

“Summarize neural networks.”

🎛️ Controls
Button	Function
💬 Send	Send typed message
🎙️ Speak	Record microphone input
🔇 Stop	Stop voice output
🧹 Clear	Reset conversation memory
🧠 Learning Outcomes

This project demonstrates:

REST API design with FastAPI

LLM integration using OpenRouter

Secure environment variable handling

Real-time speech-to-text and text-to-speech

Modular system architecture

Error handling and asynchronous operations

⚡ Future Improvements

🔐 JWT Authentication
💾 Persistent chat history (Database)
🐳 Docker containerization
☁️ Cloud deployment (Render / AWS)
🌍 Multilingual support
🧠 Long-term memory storage

👨‍💻 Developer

Chandan Kheto
Passionate about building real-time AI systems and scalable backend applications.

⭐ If you found this project interesting, feel free to star the repository!
