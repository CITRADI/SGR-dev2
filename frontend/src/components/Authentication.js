import React, { useState } from 'react';
import { postData } from '../utils/api';

const Authentication = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await postData('/login', { username, password });
      // Lógica para manejar la respuesta del backend
      console.log('Respuesta del backend:', response);
    } catch (error) {
      // Manejo de errores
      console.error('Error en la solicitud:', error);
    }
  };

  return (
    <div>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Iniciar sesión</button>
    </div>
  );
};

export default Authentication;
