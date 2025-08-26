import React, { useState } from "react";
import ResearchAssistantService from "../services/ResearchAssistantService";

function AddResearchAssistant({ onAdd }) {
  const [formData, setFormData] = useState({
    name: "",
    department: "",
    email: "",
  });

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    ResearchAssistantService.create(formData)
      .then((res) => {
        onAdd(res.data); // update parent state
        setFormData({ name: "", department: "", email: "" });
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="mb-4">
      <h4>Add Research Assistant</h4>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label>Name</label>
          <input type="text" className="form-control" name="name"
                 value={formData.name} onChange={handleChange} required />
        </div>
        <div className="mb-3">
          <label>Department ID</label>
          <input type="number" className="form-control" name="department"
                 value={formData.department} onChange={handleChange} required />
        </div>
        <div className="mb-3">
          <label>Email</label>
          <input type="email" className="form-control" name="email"
                 value={formData.email} onChange={handleChange} required />
        </div>
        <button type="submit" className="btn btn-primary">Add</button>
      </form>
    </div>
  );
}

export default AddResearchAssistant;
