
import streamlit as st
import requests
import speech_recognition as sr

from tts import speak, stop


# =========================
# Backend API URL
# =========================

BACKEND_URL = "http://127.0.0.1:8000/chat"


# =========================
# Page Setup
# =========================

st.set_page_config(
    page_title="🎓 AI Tutor",
    page_icon="🤖",
    layout="wide"
)

st.title("🧠 AI Personalized Learning Tutor")
st.markdown("Ask anything — I’ll teach you simply 👨‍🏫")


# =========================
# Session State
# =========================

if "history_display" not in st.session_state:
    st.session_state.history_display = []

if "history_api" not in st.session_state:
    st.session_state.history_api = []

if "voice_state" not in st.session_state:
    st.session_state.voice_state = {
        "engine": None,
        "speaking": False
    }


# =========================
# API Call
# =========================

def call_backend(prompt, history):

    payload = {
        "prompt": prompt,
        "history": history
    }

    r = requests.post(BACKEND_URL, json=payload, timeout=60)

    return r.json()["reply"]


# =========================
# UI Input
# =========================

user_query = st.text_input("💭 Ask your question:")

col1, col2, col3, col4 = st.columns(4)


# =========================
# Send Button (Text)
# =========================

with col1:

    if st.button("💬 Send"):

        if user_query.strip():

            with st.spinner("🤖 Thinking..."):

                response = call_backend(
                    user_query,
                    st.session_state.history_api
                )

            st.session_state.history_api += [
                {"role": "user", "content": user_query},
                {"role": "assistant", "content": response}
            ]

            st.session_state.history_display += [
                ("🧍 You", user_query),
                ("🤖 AI", response)
            ]

            speak(response, st.session_state.voice_state)


# =========================
# Voice Button (Google ASR)
# =========================

with col2:

    if st.button("🎙️ Speak"):

        r = sr.Recognizer()

        try:

            with sr.Microphone() as source:

                st.info("🎧 Listening...")

                audio = r.listen(source, timeout=8, phrase_time_limit=10)

            text = r.recognize_google(audio)

            st.success(f"You said: {text}")

            with st.spinner("🤖 Thinking..."):

                response = call_backend(
                    text,
                    st.session_state.history_api
                )

            st.session_state.history_api += [
                {"role": "user", "content": text},
                {"role": "assistant", "content": response}
            ]

            st.session_state.history_display += [
                ("🧍 You", text),
                ("🤖 AI", response)
            ]

            speak(response, st.session_state.voice_state)


        except sr.WaitTimeoutError:

            st.error("⏱️ No speech detected")


        except sr.UnknownValueError:

            st.error("❌ Could not understand audio")


        except Exception as e:

            st.error(str(e))


# =========================
# Stop / Clear
# =========================

with col3:

    if st.button("🔇 Stop"):
        stop(st.session_state.voice_state)


with col4:

    if st.button("🧹 Clear"):

        st.session_state.history_api.clear()
        st.session_state.history_display.clear()


# =========================
# History
# =========================

st.markdown("---")
st.subheader("🗨️ History")

for role, msg in reversed(st.session_state.history_display[-10:]):

    st.markdown(f"**{role}:** {msg}")


st.caption("⚡ Powered by Llama-3 • OpenRouter API • Built by Chandan Kheto ❤️")
