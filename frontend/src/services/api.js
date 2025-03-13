// src/services/api.js
import axios from 'axios';

export async function createCharacter(name, chosenClass) {
  const url = `http://127.0.0.1:8000/create_character/?chosen_class=${encodeURIComponent(chosenClass)}&name=${encodeURIComponent(name)}`;
  const response = await axios.post(url);
  return response.data;
}

export async function loadCharacter(charId) {
  const url = `http://127.0.0.1:8000/load_character/${charId}`;
  const response = await axios.get(url);
  return response.data;
}

export async function fetchAiResponse(action, sessionId) {
  const url = `http://127.0.0.1:8000/dungeon_master/?action=${encodeURIComponent(action)}&session_id=${sessionId}`;
  const response = await axios.get(url);
  return response.data;
}

export async function rollDiceCheck(sessionId, roll, check_type, dc) {
  const url = `http://127.0.0.1:8000/roll_check/?session_id=${sessionId}&roll=${roll}&check_type=${check_type}&dc=${dc}`;
  const response = await axios.get(url);
  return response.data;
}
