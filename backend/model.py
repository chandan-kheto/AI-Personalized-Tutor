
import requests

from backend.config import OPENROUTER_API_KEY, MODEL_NAME


def ask_model(prompt: str, history=None) -> str:

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    limited_history = (history or [])[-10:]

    messages = [
        {
            "role": "system",
            "content": "You are a friendly and helpful AI tutor."
        }
    ]

    messages.extend(limited_history)

    messages.append({
        "role": "user",
        "content": prompt.strip()
    })

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": 600,
        "temperature": 0.7,
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:

        return f"⚠️ Model Error: {e}"
