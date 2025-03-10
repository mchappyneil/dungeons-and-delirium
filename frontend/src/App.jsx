// src/App.jsx
import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import ActionForm from './components/ActionForm';
import CharacterCreation from './components/CharacterCreation';
import { fetchAiResponse, rollDiceCheck } from './services/api';
import './App.css';

function App() {
  const [playerState, setPlayerState] = useState(null);
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [pendingCheck, setPendingCheck] = useState(null);

  const handleCharacterCreated = (newSessionId, newPlayerState) => {
    setSessionId(newSessionId);
    setPlayerState(newPlayerState);
  };

  const handleSendAction = async (action) => {
    setMessages((prev) => [...prev, { sender: 'user', text: action }]);
    try {
      const data = await fetchAiResponse(action, sessionId);
      setMessages((prev) => [...prev, { sender: 'dm', text: data.narrative }]);
      if (data.check) setPendingCheck(data.check);
      if (data.player_state) setPlayerState(data.player_state);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'dm', text: 'Error: Could not fetch response from server.' },
      ]);
    }
  };

  const handleRollDice = async () => {
    if (!pendingCheck) return;
    const roll = Math.floor(Math.random() * 20) + 1;
    try {
      const data = await rollDiceCheck(sessionId, roll, pendingCheck.check_type, pendingCheck.dc);
      setMessages((prev) => [...prev, { sender: 'dm', text: data.result }]);
      if (data.player_state) setPlayerState(data.player_state);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'dm', text: 'Error: Could not process dice roll.' },
      ]);
    }
    setPendingCheck(null);
  };

  // Only show character creation if no character is set
  if (!playerState) {
    return <CharacterCreation onCharacterCreated={handleCharacterCreated} />;
  }

  return (
    <div className="container">
      <h1>Dungeons and Delirium</h1>
      <div className="main-content">
        {/* Left column: chat + dice roll + action form */}
        <div className="left-column">
          <ChatWindow messages={messages} />
          {pendingCheck && (
            <div className="roll-check">
              <p>Roll a d20 for a {pendingCheck.check_type} check (DC {pendingCheck.dc})</p>
              <button onClick={handleRollDice}>Roll Dice</button>
            </div>
          )}
          <ActionForm onSubmit={handleSendAction} />
        </div>

        {/* Right column: player stats */}
        <div className="right-column">
          <div className="player-state">
            <h2>Player Stats</h2>
            <p>Class: {playerState.class_name}</p>
            <p>Level: {playerState.level}</p>
            <p>Hit Points: {playerState.hit_points}</p>
            <p>Armor Class: {playerState.armor_class}</p>
            <p>Successful Checks: {playerState.successful_checks}</p>
            <h3>Abilities:</h3>
            <ul>
              {Object.entries(playerState.stats).map(([stat, value]) => (
                <li key={stat}>
                  {stat}: {value}
                </li>
              ))}
            </ul>
            <h3>Equipment:</h3>
            <p>
              {playerState.equipment.length > 0
                ? playerState.equipment.join(', ')
                : 'None'}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
