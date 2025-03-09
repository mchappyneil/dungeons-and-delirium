import React from 'react';
import './ChatWindow.css';

function ChatWindow({ messages }) {
  return (
    <div className="chatbox">
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.sender}`}>
          {msg.text}
        </div>
      ))}
    </div>
  );
}

export default ChatWindow;