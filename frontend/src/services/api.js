export async function createCharacter(chosenClass) {
  const url = `http://127.0.0.1:8000/create_character/?chosen_class=${encodeURIComponent(chosenClass)}`;
  const response = await fetch(url, { method: 'POST' });
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  return response.json();
}

export async function fetchAiResponse(action, sessionId) {
  const url = `http://127.0.0.1:8000/dungeon_master/?action=${encodeURIComponent(action)}&session_id=${sessionId}`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  return response.json();
}

export async function rollDiceCheck(sessionId, roll, check_type, dc) {
  const url = `http://127.0.0.1:8000/roll_dice_check/?session_id=${sessionId}&roll=${roll}&check_type=${check_type}&dc=${dc}`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  return response.json();
}

