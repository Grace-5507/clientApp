import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import AddClient from "../../components/addClient/AddClients";
import Header from "../../components/header/Header";

function Clients() {
  const [clients, setClients] = useState([]);

  useEffect(() => {
    axios
      .get("/clients/clients")
      .then((res) => setClients(res.data))
      .catch((err) => console.error(err));
  }, []);
   const navigate = useNavigate();
   const history = useNavigate();
   const handleClick = () => {
    navigate("/clientform");
  };

  return (
    <div>
      <div>
        <Header />
        <div>
          <AddClient />
        </div>
      </div>
      {clients.length > 0 ? (
        <Table striped bordered hover>
          <thead>
            <tr>
              <th style={{ textAlign: "left" }}>sirName</th>
              <th style={{ textAlign: "left" }}>fullName</th>
              <th style={{ textAlign: "left" }}>email</th>
              <th style={{ textAlign: "left" }}>Client Code</th>
              <th style={{ textAlign: "center" }}>Number of Linked Contacts</th>
            </tr>
          </thead>
          <tbody>
            {clients
              .sort((a, b) => a.name.localeCompare(b.name))
              .map((client) => (
                <tr key={client.id}>
                  <td style={{ textAlign: "left" }}>{client.sirName}</td>
                  <td style={{ textAlign: "left" }}>{client.fullName}</td>
                  <td style={{ textAlign: "left" }}>{client.email}</td>
                  <td style={{ textAlign: "left" }}>{client.clientCode}</td>
                  <td style={{ textAlign: "center" }}>
                    {client.linkedContacts}
                  </td>
                </tr>
              ))}
          </tbody>
        </Table>
      ) : (
        <p>No Clients found</p>
      )}
      <button className="btn btn-outline-info rounded" onClick={handleClick}>
        Client form
      </button>
    </div>
  );
}

export default Clients;
