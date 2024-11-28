import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

function App() {
  const [inputData, setInputData] = useState({
    address: "",
    beds: 0,
    baths: 0,
    sqft: 0,
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
        `${process.env.REACT_APP_BACKEND_URL}/predict-house-price`,
        inputData
      );
      setPrediction(response.data.predictedPrice);
    } catch (error) {
      console.error("Error fetching prediction:", error);
    }
  };

  return (
    <div>
      <nav className="navbar">
        <div className="navbar-title">Atlanta Home Price Estimator</div>
          <div className="navbar-links">
            <a href="home">Home</a>
            <a href="about">About</a>
          </div>
      </nav>
      <div className="content">
        <div className="title-panel">
          <h1>Atlanta Home Price Estimator</h1>
          <p className="description">
          A tool for estimating the price of any home in Metro Atlanta
          </p>
        </div>
        <div className="form-panel">
          <h2>Fill out home details</h2>
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
          { prediction && <p className="estimation">Estimated Price: ${prediction}</p> }
          <p className="disclaimer">
            Disclaimer: Price estimations have an average error of ~22%.
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;