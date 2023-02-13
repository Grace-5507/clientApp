import React from "react";
import Landing from "./pages/landing/Landing";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Clients from "./pages/clients/Clients";
import Contacts from "./pages/contacts/Contacts";
import Clientform from "./pages/clientForm/Clientform";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" exact element={<Landing />} />
        <Route path="/clients" element={<Clients />} />
        <Route path="/contacts" element={<Contacts />} />
        <Route path="/clientform" element={<Clientform />} />
      </Routes>
    </Router>
  );
}

export default App;
