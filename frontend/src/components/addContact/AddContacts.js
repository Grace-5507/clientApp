import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";

function AddContact() {
  const [fullName, setFullName] = useState("");
  const [sirName, setSirName] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post("/contacts/contacts", {
        fullName,
        sirName,
        
        email,
      })
      .then((res) => console.log(res.data))
      .catch((err) => console.error(err));
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="fullName">
        <Form.Label>Full Name</Form.Label>
        <Form.Control
          type="text"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="sirName">
        <Form.Label>Sir Name</Form.Label>
        <Form.Control
          type="text"
          value={sirName}
          onChange={(e) => setSirName(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="email">
        <Form.Label>Email Address</Form.Label>
        <Form.Control
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </Form.Group>
      <Button type="submit">Add Contact</Button>
    </Form>
  );
}

export default AddContact;
