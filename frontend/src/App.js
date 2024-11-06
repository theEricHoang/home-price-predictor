import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputData, setInputData] = useState({});
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setInputData({
      ...inputData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async() => {
    try {
      const response = await axios.post(
        `%{process.env.REACT_APP_BACKEND_URL}/predict`,
        inputData
      );
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error("Error fetching prediction:", error);
    }
  };

  return (
    <div>
      <h1>Prediction App</h1>
      <input type="text" name="feature" onChange={handleChange} />
      <button onClick={handleSubmit}>Predict</button>
      {prediction && <p>Prediction: {prediction}</p>}
    </div>
  );
}

export default App;