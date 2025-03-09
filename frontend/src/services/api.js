export async function fetchAiResponse(action, sessionId) {
    const url = `http://127.0.0.1:8000/dungeon_master/?action=${encodeURIComponent(action)}&session_id=${sessionId}`;
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  }