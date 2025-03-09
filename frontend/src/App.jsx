// src/App.jsx
import React, { useState, useEffect } from 'react';
import ChatWindow from './components/ChatWindow';
import ActionForm from './components/ActionForm';
import { fetchAiResponse } from './services/api';
import './App.css';

function App() {
  // Store all chat messages
  const [messages, setMessages] = useState([]);

  // Generate or retrieve a session ID to maintain conversation memory
  const [sessionId, setSessionId] = useState(() => {
    const saved = localStorage.getItem('dndSessionId');
    if (saved) {
      return saved;
    } else {
      // If none found, create a new one
      const newId = crypto.randomUUID();
      localStorage.setItem('dndSessionId', newId);
      return newId;
    }
  });

  // Called when the user submits an action
  const handleSendAction = async (action) => {
    // Add user action to messages
    setMessages((prev) => [...prev, { sender: 'user', text: action }]);

    try {
      const data = await fetchAiResponse(action, sessionId);
      setMessages((prev) => [...prev, { sender: 'dm', text: data.response }]);

    } catch (err) {
      console.error("Error fetching response:", err);
      setMessages((prev) => [
        ...prev,
        { sender: 'dm', text: 'Error: Could not fetch response from server.' },
      ]);
    }
  };

  return (
    <div className="container">
      <h1>Dungeons and Delirium</h1>
      <ChatWindow messages={messages} />
      <ActionForm onSubmit={handleSendAction} />
    </div>
  );
}

export default App;
