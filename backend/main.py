from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "http://localhost:5173",   # React dev server
    "http://127.0.0.1:5173",   # Sometimes needed if using 127.0.0.1 instead of localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_dnd_response(prompt):
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "An error occurred.")

@app.get("/dungeon_master/")
def get_dungeon_response(action: str):
    prompt = f"""
    You are a chaotic, unpredictable, funny Dungeon Master of a game of Dungeons and Dragons.
    
    The player just said: {action}. Introduce an unpredictable but fun plot twist.
    
    Occasionally include some seriously wacky and/or unbelieveable situations featuring famous
    people from the real world. These events should be slightly more uncommon than the regular
    chaotic events.
    
    The point of your response is to make players so dumbfounded that they can only 
    laugh about the situation they face.
    """
    return {"response": generate_dnd_response(prompt)}