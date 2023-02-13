import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";

function AddClient() {
  const [name, setName] = useState("");
  const [clientCode, setClientCode] = useState("");
  const [linkedContacts, setLinkedContacts] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post("/api/clients", {
        name,
        clientCode,
        linkedContacts,
      })
      .then((res) => console.log(res.data))
      .catch((err) => console.error(err));
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="name">
        <Form.Label>Name</Form.Label>
        <Form.Control
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="clientCode">
        <Form.Label>Sir name</Form.Label>
        <Form.Control
          type="text"
          value={clientCode}
          onChange={(e) => setClientCode(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="linkedContacts">
        <Form.Label>Email Address</Form.Label>
        <Form.Control
          type="text"
          value={linkedContacts}
          onChange={(e) => setLinkedContacts(e.target.value)}
        />
      </Form.Group>
      <Button type="submit">Add Client</Button>
    </Form>
  );
}

export default AddClient;
