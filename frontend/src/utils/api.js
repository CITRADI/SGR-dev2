import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Reemplaza con la URL de tu backend

// Ejemplo de función para realizar una solicitud POST al backend
export const postData = async (endpoint, data) => {
  try {
    const response = await axios.post(`${API_URL}${endpoint}`, data);
    return response.data;
  } catch (error) {
    console.error('Error en la solicitud:', error);
    throw error;
  }
};

// Ejemplo de función para realizar una solicitud GET al backend
export const getData = async (endpoint) => {
  try {
    const response = await axios.get(`${API_URL}${endpoint}`);
    return response.data;
  } catch (error) {
    console.error('Error en la solicitud:', error);
    throw error;
  }
};
