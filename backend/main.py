from fastapi import FastAPI
import requests

app = FastAPI()

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
    
    Occasionally include some seriously wacky and/or unbelieveable situations, including real life famous people appearing
    in the world. For example, Jeff Bezos being a trader NPC - he could for example be willing to trade you items for gold, 
    or a 30 second advertisement you have to watch entirely (he could cast a spell or something that makes it impossible 
    for the player to look away).
    
    These events should be sporadic but not rare, and the point of your response is to make players so dumbfounded that they
    can only laugh about the situation.
    """
    return {"response": generate_dnd_response(prompt)}