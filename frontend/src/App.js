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
            <a href="#home">Home</a>
            <a href="#about">About</a>
          </div>
      </nav>

      <div id="home" className="content">
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

      <div id="about" className="about-section">
        <h2>About This Project</h2>
        <p>
          This project was built using data collected from 8,000 house listings on Zillow to train a machine learning model to make predictions for house prices.
        </p>

        <div className="bios">
          <div className="bio">
            <img src="erichoangbio.jpeg" alt="Eric Hoang" />
            <h3>Eric Hoang</h3>
            <p>Built a robust web scraper to collect data on over 8,000 Atlanta homes. Trained a Gradient Boosting Regressor model with sk-learn to predict home prices. Designed a RESTful API with Flask to handle prediction requests.</p>
            <a href="https://www.linkedin.com/in/erichoang2/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://github.com/theEricHoang" target="_blank" rel="noopener noreferrer">GitHub</a>
          </div>
          
          <div className="bio">
            <img src="ryanphambio.jpeg" alt="Ryan Pham" />
            <h3>Ryan Pham</h3>
            <p>
              Implemented a seamless frontend UI, including separate sections that featured an interactive form panel to fetch predicted house prices and information about the contributors. Designed a modern, user-friendly experience with smooth navigation and a responsive design.
            </p>
            <a href="https://www.linkedin.com/in/the-ryan-pham/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://github.com/ryangpham" target="_blank" rel="noopener noreferrer">GitHub</a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;