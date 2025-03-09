from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import uuid # for generating session IDs if needed

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

conversations = {}

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
def get_dungeon_response(action: str, session_id: str = None):
    """
    - action: the user's current input or choice
    - session_id: unique ID for each conversation
    """
    
    # If no sesion_id provided, generate one
    if not session_id:
        session_id = str(uuid.uuid4())
    
    # If brand new session, initialize it
    if session_id not in conversations:
        conversations[session_id] = []
    
    # Append user message to conversation
    conversations[session_id].append({"role": "user", "content": action})
    
    # Build a prompt that includes the entire conversation history
    conversation_text = ""
    for msg in conversations[session_id]:
        if msg["role"] == "user":
            conversation_text += f"User: {msg['content']}\n"
        else:
            conversation_text += f"DM: {msg['content']}\n"
    
    prompt = f"""
    You are a chaotic, unpredictable, funny Dungeon Master of a game of Dungeons and Dragons.
        
    Occasionally include some seriously wacky and/or unbelieveable situations featuring famous
    people from the real world. These events should be slightly more uncommon than the regular
    chaotic events.
    
    The point of your response is to make players so dumbfounded that they can only 
    laugh about the situation they face.
    
    Keep track of the conversation context and reference past user actions if relevant.
    Do not end your response with a concluding sentence, ending the adventure. 
    Strive to continue the story by constantly providing new situations and unexpected twists.
    
    {conversation_text}
    DM:
    """
    ai_response = generate_dnd_response(prompt)
    
    conversations[session_id].append({"role": "assisstant", "content": ai_response})
    return {
        "response": ai_response,
        "session_id": session_id
    }