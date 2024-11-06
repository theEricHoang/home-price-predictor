import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/api')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
        setMessage('ballsack');
      });
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  );
}

export default App;