import React, { useState } from 'react';

function Interaction() {
  const [userInput, setUserInput] = useState('');
  const [aiFeedback, setAiFeedback] = useState('');

  const handleUserInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleAiFeedbackChange = (event) => {
    setAiFeedback(event.target.value);
  };

  const handleInteraction = () => {
    // Lógica para enviar la interacción al backend y obtener la retroalimentación de IA
    // ...
    console.log(`User Input: ${userInput}`);
    console.log(`AI Feedback: ${aiFeedback}`);
    // ...
  };

  return (
    <div>
      <h2>Interaction Component</h2>
      <form>
        <div>
          <label htmlFor="userInput">User Input:</label>
          <input type="text" id="userInput" value={userInput} onChange={handleUserInputChange} />
        </div>
        <div>
          <label htmlFor="aiFeedback">AI Feedback:</label>
          <input type="text" id="aiFeedback" value={aiFeedback} onChange={handleAiFeedbackChange} />
        </div>
        <button type="button" onClick={handleInteraction}>Interact</button>
      </form>
    </div>
  );
}

export default Interaction;
