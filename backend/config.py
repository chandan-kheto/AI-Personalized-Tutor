
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


# API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# Model Name
MODEL_NAME = "meta-llama/llama-3-8b-instruct"


# Validation
if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env file")
