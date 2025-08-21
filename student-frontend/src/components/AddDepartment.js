import React, { useState } from "react";
import { addDepartment } from "../services/departmentService";

const AddDepartment = ({ refresh }) => {
  const [code, setCode] = useState("");
  const [name, setName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    addDepartment({ code, name })
      .then(() => {
        setCode("");
        setName("");
        refresh(); // refresh the list
      })
      .catch(err => console.log(err));
  };

  return (
    <form onSubmit={handleSubmit} className="d-flex gap-2">
      <input
        type="text"
        placeholder="Department Code"
        className="form-control"
        value={code}
        onChange={e => setCode(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Department Name"
        className="form-control"
        value={name}
        onChange={e => setName(e.target.value)}
        required
      />
      <button type="submit" className="btn btn-primary">Add</button>
    </form>
  );
};

export default AddDepartment;
