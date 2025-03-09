// src/components/ActionForm.jsx
import React, { useState } from 'react';

function ActionForm({ onSubmit }) {
  const [action, setAction] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!action.trim()) return;
    onSubmit(action);
    setAction('');
  };

  return (
    <form onSubmit={handleSubmit} className="action-form">
      <input
        type="text"
        value={action}
        onChange={(e) => setAction(e.target.value)}
        placeholder="Enter your action..."
        required
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default ActionForm;
