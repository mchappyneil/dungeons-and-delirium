import { useState, UseState } from 'react';
import './App.css';

function App() {
  const [action, setAction] = useState('')
  const [messages, setMessages] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!action.trim()) return;

    // Add user's action to messages
    setMessages((prev) => [...prev, {sender: 'user', text: action }]);

    try {
      const res = await fetch(`http://127.0.0.1:8000/dungeon_master/?action=${encodeURIComponent(action)}`)
      const data = await res.json();
      setMessages((prev) => [...prev, {sender: 'dm', text: data.response }]);
    } catch (error) {
      setMessages((prev) => [...prev, { sender: 'dm', text: 'Error: Could not fetch response from server.'}]);
      console.error(error);
    }
    setAction('');
  };

  return (
    <div className="container">
      <h1>Dungeons and Delirium</h1>
      <div className="chatbox">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit} className='action-form'>
        <input
          type="text"
          value={action}
          onChange={(e) => setAction(e.target.value)}
          placeholder="Enter your action..."
          required
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;