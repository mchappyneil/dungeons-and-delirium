from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from models.player import create_player, Player
import requests
import uuid # for generating session IDs if needed
import json

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
player_states = {}

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_dnd_response(prompt):
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "An error occurred.")

@app.post("/create_character")
def create_character(chosen_class: str, session_id: str = Query(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
    if session_id in player_states:
        return {
            "error": "Character already exists",
            "session_id": session_id,
            "player_state": player_states[session_id].to_dict()
        }
    try:
        player = create_player(chosen_class)
    except ValueError as e:
        return {"error": str(e), "session_id": session_id}
    
    player_states[session_id] = player
    conversations[session_id] = [] # Initialize conversation history
    return {"session_id": session_id, "player_state": player.to_dict()}
    
    
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
    if session_id not in player_states:
        return {"error": "No character found for this session."}
    
    player = player_states[session_id]
    
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
    
    The player's current stats are:
    Strength: {player.stats['Strength']},
    Dexterity: {player.stats['Dexterity']},
    Constitution: {player.stats['Constitution']},
    Intelligence: {player.stats['Intelligence']},
    Wisdom: {player.stats['Wisdom']},
    Charisma: {player.stats['Charisma']}.
    Armor Class: {player.armor_class}
    Hit Points: {player.hit_points}
    Level: {player.level}

    When the player attempts an action, decide which ability check is required and specify a target DC on a d20 roll.
    Remember: the player's effective roll is d20 + modifier, where modifier = (stat - 10) // 2.
    At the end of your response, on a new line, output a JSON object with keys "check_type" and "dc". For example:
    {{"check_type": "Strength", "dc": 15}}

    Now, incorporate the following conversation:
    {conversation_text}
    DM:
    """
    ai_response = generate_dnd_response(prompt)
    
    # Attempt to extract check details (assumed last line in JSON)
    lines = ai_response.strip().split("\n")
    try:
        check_info = json.loads(lines[-1])
        narrative = "\n".join(lines[:-1]).strip()
    except Exception as e:
        check_info = None
        narrative = ai_response
    
    conversations[session_id].append({"role": "assisstant", "content": ai_response})
    return {
        "narrative": narrative,
        "check": check_info,
        "session_id": session_id,
        "player_state": player.to_dict()
    }
    
@app.get("/roll_check/")
def roll_check(sesion_id: str, roll: int, check_type: str, dc: int):
    if sesion_id not in player_states:
        return {"error": "Invalid session."}
    
    player = player_states[sesion_id]
    stat_value = player.stats.get(check_type, 10)
    modifier = (stat_value - 10) // 2
    effective_roll = roll + modifier
    success = effective_roll >= dc
    
    message = f"You rolled a {roll} with a modifier of {modifier} (total {effective_roll})."
    if success:
        message += " Check succeeded!"
        player.successful_checks += 1
        if player.successful_checks >= 10:
            player.level_up()
            message += " You leveled up! All your ability scores have increased by 1."
    else:
        message += " Check failed!"
    
    return {
        "result": message,
        "player_state": player.to_dict(),
        "success": success,
        "roll": effective_roll
    }