# Dungeons and Delirium

An AI-powered, Dungeons & Dragons-inspired text adventure featuring an absurd, _chaotic_ AI-powered Dungeon Master. This project uses FastAPI and Python for the backend, and a React (Vite) frontend.

---

## Features
- **Character Creation:** Choose from Fighter, Bard, Ranger, Wizard, Rogue, or Cleric, each with unique stats and descriptions.  
- **Chaotic AI Dungeon Master:** GPT-like responses that track conversation context and prompt dice checks for actions.  
- **Dice Rolls & Stat Checks:** A d20 roll plus modifiers determines the success or failure of your actions.  
- **Player State Tracking:** Displays your current level, hit points, armor class, stats, and equipment.

---

## Getting Started

### Prerequisites
- **Python 3.9+**  
- **Node.js 16+**  
- **Ollama** or another method to run a local LLM (e.g., Mistral-7B), more info [here](https://ollama.com/library/mistral:7b) on Ollama and Mistral-7B

---

### 1. Clone the Repository
```bash
git clone https://github.com/mchappyneil/dungeons-and-delirium.git
cd dungeons-and-delirium
```
### 2. Set up the backend
  1. Navigate to the backend folder
  ```bash
  cd backend
  ```
  2. Create a virtual environment (optional, but recommended).

  3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
  The backend will be running at http://127.0.0.1:8000 by default. 
  
  5. **Open a new terminal** and set up a local LLM:
  ```bash
  ollama serve
  ```
  By default, the backend references an endpoint at http://localhost:11434/api/generate (used by Ollama for Mistral-7B).
  
  If you have a different LLM setup, edit the `OLLAMA_URL` variable in `backend/main.py` to match your endpoint.

### 3. Set up the frontend
  1. **Open a new terminal** and navigate to the `frontend/` folder:
  ```bash
  cd frontend/
  ```
  2. Install dependencies:
  ```bash
  npm install
  ```
  3. Run the development server:
  ```bash
  npm run dev
  ```
  The frontend will be served at http://127.0.0.1:5173 by default.

## Usage
1. Open http://127.0.0.1:5173 in your browser.
2. **Character Creation:** Select one of the six classes to create your character.
3. **Interact with the Dungeon Master:** Use the chat interface to issue actions.
4. **Roll Dice:** When prompted, roll a d20 to determine the success or failure of your action.
5. **Monitor your Stats:** Your current level, hit points, armor class, and abilities are displayed in the player stats panel.

## Roadmap/Coming Features
Please note that these features are mentioned in no specific order.
- [ ] **Multiplayer Support:** Allow multiple players to join a shared campaign and interact in real time.
- [ ] **Complete UI Overhaul:** Redesign the user interface for a more immersive and polished experience.
- [ ] **Class-Specific Abilities:** Implement unique abilities, spells, and leveling mechanics for each character class.
- [ ] **Persistent Save/Load:** Integrate a database to save player sessions and allow players to rejoin their campaigns.
- [ ] **Enhanced Narrative Memory:** Improve conversation tracking to handle longer, more complex campaigns including NPCs, quests, and storylines.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License
This project is licensed under the terms of the MIT License.
