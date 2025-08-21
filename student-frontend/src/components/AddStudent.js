import React, { useState } from "react";
import { Form, Button, Card } from "react-bootstrap";

function AddStudent({ onAdd }) {
  const [form, setForm] = useState({
    name: "",
    department: "",
    year: "",
    age: "",
    phone: "",
    email: "",
    address: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add student to parent component
    onAdd({ ...form, id: Date.now() });
    // Reset form
    setForm({
      name: "",
      department: "",
      year: "",
      age: "",
      phone: "",
      email: "",
      address: "",
    });
  };

  return (
    <Card className="p-4 shadow-sm mt-4">
      <h3>Add Student</h3>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-2">
          <Form.Label>Name</Form.Label>
          <Form.Control type="text" name="name" value={form.name} onChange={handleChange} required />
        </Form.Group>

        <Form.Group className="mb-2">
          <Form.Label>Department</Form.Label>
          <Form.Control type="text" name="department" value={form.department} onChange={handleChange} required />
        </Form.Group>

        <Form.Group className="mb-2">
          <Form.Label>Year</Form.Label>
          <Form.Control type="number" name="year" value={form.year} onChange={handleChange} required />
        </Form.Group>

        <Form.Group className="mb-2">
          <Form.Label>Age</Form.Label>
          <Form.Control type="number" name="age" value={form.age} onChange={handleChange} required />
        </Form.Group>

        <Form.Group className="mb-2">
          <Form.Label>Phone</Form.Label>
          <Form.Control type="text" name="phone" value={form.phone} onChange={handleChange} />
        </Form.Group>

        <Form.Group className="mb-2">
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" name="email" value={form.email} onChange={handleChange} />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Address</Form.Label>
          <Form.Control as="textarea" name="address" value={form.address} onChange={handleChange} rows={2} />
        </Form.Group>

        <Button variant="primary" type="submit">
          Add Student
        </Button>
      </Form>
    </Card>
  );
}

export default AddStudent;
