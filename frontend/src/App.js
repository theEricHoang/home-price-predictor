import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

function App() {
  const [inputData, setInputData] = useState({
    address: "",
    beds: "",
    bath: "",
    sqft: "",
  });
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
      <nav className="navbar">
        <div className="navbar-title">Home Price Prediction</div>
          <div className="navbar-links">
            <a href="home">Home</a>
            <a href="about">About</a>
          </div>
      </nav>
      <div className="content">
        <div className="title-panel">
          <h1>Home Price Predictor</h1>
          <p className="description">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          </p>
        </div>
        <div className="form-panel">
          <h2>Fill Out Home Details</h2>
          <form
            onSubmit = {(e) => {
              e.preventDefault();
              handleSubmit();
            }}
          >
            <div>
              <label>Address:</label>
              <input type="text" name="address" value={inputData.address} onChange={handleChange} required/>
            </div>

            <div>
              <label>Beds:</label>
              <input type="number" name="beds" value={inputData.beds} onChange={handleChange} required/>
            </div>

            <div>
              <label>Baths:</label>
              <input type="number" name="baths" value={inputData.baths} onChange={handleChange} required/>
            </div>

            <div>
              <label>Square Feet:</label>
              <input type="number" name="sqft" value={inputData.sqft} onChange={handleChange} required/>
            </div>

            <button type="submit">Estimate</button>
          </form>
          { prediction && <p>Estimated Price: ${prediction}</p> }
          <p className="disclaimer">
            Disclaimer: Price estimations have an average error of ~22%.
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;