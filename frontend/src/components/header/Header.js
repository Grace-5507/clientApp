import React from "react";
import Photo from "../../assets/lady.jpg";
import "./Header.css";
import { useEffect } from "react";
import { useState } from "react";

function Header() {
  const [user, setUser] = useState({});
  // console.log('USER',sessionStorage.getItem('userObj'))

  useEffect(() => {
    setUser(JSON.parse(sessionStorage.getItem("userObj")));
    console.log("EFFE", user);
  }, []);

  return (
    <div className="head">
      <div>
        <h3>Client App</h3>
      </div>
    </div>
  );
}
export default Header;