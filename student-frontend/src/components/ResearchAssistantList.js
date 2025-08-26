import React, { useEffect, useState } from "react";
import ResearchAssistantService from "../services/ResearchAssistantService";

function ResearchAssistantList({ researchAssistants }) {
  const [assistants, setAssistants] = useState(researchAssistants);

  useEffect(() => {
    ResearchAssistantService.getAll()
      .then((res) => setAssistants(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h4>Research Assistant List</h4>
      <table className="table table-bordered">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {assistants.map((ra) => (
            <tr key={ra.id}>
              <td>{ra.id}</td>
              <td>{ra.name}</td>
              <td>{ra.department}</td>
              <td>{ra.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ResearchAssistantList;
