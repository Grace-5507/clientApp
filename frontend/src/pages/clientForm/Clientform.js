import React, { Component } from 'react'
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

function Clientform() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userData, setUserData] = useState({});
  const navigate = useNavigate();
  const history = useNavigate();

  
  const handleClick = () => {
    navigate("/contacts");
  };
    return (
      <div>
        Clientform
        <button className="btn btn-outline-info rounded" onClick={handleClick}>
          contacts
        </button>
      </div>
    );
  }


export default Clientform