
# Main backend file for AI Tutor (FastAPI)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

# Import LLM logic
from backend.model import ask_model


# Initialize app
app = FastAPI(title="AI Tutor API", version="1.0")


# Request schema
class ChatRequest(BaseModel):
    prompt: str
    history: List[Dict] = []


# Response schema
class ChatResponse(BaseModel):
    reply: str


# Health check
@app.get("/")
def home():
    return {"status": "Backend Running 🚀"}


# Main chat API
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    # Get AI response
    answer = ask_model(
        prompt=req.prompt,
        history=req.history
    )

    # Send back to frontend
    return {"reply": answer}
