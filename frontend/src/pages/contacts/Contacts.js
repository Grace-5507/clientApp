import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import axios from "axios";

import Header from "../../components/header/Header";
import AddContact from "../../components/addContact/AddContacts";

function Contacts() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    axios
      .get("/contacts")
      .then((res) => setContacts(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <div>
        <Header />
        <div>
          <AddContact />
        </div>
      </div>
      {contacts.length > 0 ? (
        <Table striped bordered hover>
          <thead>
            <tr>
              <th style={{ textAlign: "left" }}>Full Name</th>
              <th style={{ textAlign: "left" }}>Sir Name</th>
              <th style={{ textAlign: "center" }}>Number of Linked Clients</th>
              <th style={{ textAlign: "left" }}>Email Address</th>
            </tr>
          </thead>
          <tbody>
            {contacts
              .sort((a, b) => a.name.localeCompare(b.name))
              .map((contact) => (
                <tr key={contact.id}>
                  <td style={{ textAlign: "left" }}>{contact.fullName}</td>
                  <td style={{ textAlign: "left" }}>{contact.sirName}</td>
                  <td style={{ textAlign: "center" }}>
                    {contact.linkedClients}
                  </td>
                  <td style={{ textAlign: "left" }}>{contact.email}</td>
                </tr>
              ))}
          </tbody>
        </Table>
      ) : (
        <p>No Contacts found</p>
      )}

    </div>
  );

 
    
}

export default Contacts;
