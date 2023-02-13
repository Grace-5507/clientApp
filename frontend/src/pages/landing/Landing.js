/* eslint-disable no-undef */
import React from "react";
import lady from "../../assets/lady.jpg";
import "./Landing.css";

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";


function Landing() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userData, setUserData] = useState({});
  const navigate = useNavigate();
  const history = useNavigate();

  
  const handleClick = () => {
    navigate("/clients");
  };

  
  return (
    <div className="page">
      <div className="d-flex justify-content-center align-self-center">
        <div className="middle text-center">
          <h2>Breeze ClientsAPP</h2>
          <h3>Amazing applications for clients </h3>
          <button
            className="btn btn-outline-info rounded"
            onClick={handleClick}
          >
            Get Started
          </button>
        </div>
      </div>
    </div>
  );
}

export default Landing;
