import React, { useState } from "react";
import { Form, Button, Container, Row, Col } from "react-bootstrap";

const AddClient = () => {
  const [sirName, setSirName] = useState("");
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [clientCode, setClientCode] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send the new client data to the server for storage
    fetch("/clients/clients", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        sirName,
        fullName,
        email,
        clientCode,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        // Clear the form fields after a successful submission
        setSirName("");
        setFullName("");
        setEmail("");
        setClientCode("");
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <Container>
      <Row>
        <Col md={{ span: 6, offset: 3 }}>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="formSirName">
              <Form.Label>Sir Name</Form.Label>
              <Form.Control
                type="text"
                value={sirName}
                onChange={(e) => setSirName(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId="formFullName">
              <Form.Label>Full Name</Form.Label>
              <Form.Control
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId="formEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId="formClientCode">
              <Form.Label>Client Code</Form.Label>
              <Form.Control
                type="text"
                value={clientCode}
                onChange={(e) => setClientCode(e.target.value)}
              />
            </Form.Group>
            <Button variant="primary" type="submit">
              Add Client
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default AddClient;
