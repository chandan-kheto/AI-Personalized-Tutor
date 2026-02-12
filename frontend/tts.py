
import threading
import pyttsx3
import pythoncom


def _init_engine():
    """Initialize Windows TTS engine"""

    pythoncom.CoInitialize()

    engine = pyttsx3.init("sapi5")

    engine.setProperty("rate", 175)

    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)

    return engine


def speak(text, state):
    """Speak text in background thread"""

    def _run():

        try:
            state["speaking"] = True

            engine = _init_engine()

            state["engine"] = engine

            engine.say(text)
            engine.runAndWait()

        finally:
            state["speaking"] = False
            state["engine"] = None


    threading.Thread(target=_run, daemon=True).start()


def stop(state):
    """Stop current speech"""

    try:
        if state.get("speaking") and state.get("engine"):
            state["engine"].stop()
    except:
        pass
