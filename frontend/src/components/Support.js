import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Support() {
  const [faqs, setFaqs] = useState([]);

  useEffect(() => {
    fetchFaqs();
  }, []);

  const fetchFaqs = async () => {
    try {
      const response = await axios.get('/api/faqs');
      setFaqs(response.data);
    } catch (error) {
      console.error('Error fetching FAQs:', error);
    }
  };

  return (
    <div>
      <h2>Support Component</h2>
      <h3>FAQs:</h3>
      <ul>
        {faqs.map((faq) => (
          <li key={faq.id}>
            <strong>Question:</strong> {faq.question}<br />
            <strong>Answer:</strong> {faq.answer}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Support;
