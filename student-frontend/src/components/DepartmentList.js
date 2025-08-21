import React, { useEffect, useState } from "react";
import { getDepartments, deleteDepartment } from "../services/departmentService";
import AddDepartment from "./AddDepartment";

const DepartmentList = () => {
  const [departments, setDepartments] = useState([]);

  const fetchDepartments = () => {
    getDepartments().then(res => setDepartments(res.data)).catch(err => console.log(err));
  };

  useEffect(() => {
    fetchDepartments();
  }, []);

  const handleDelete = (id) => {
    deleteDepartment(id).then(() => fetchDepartments()).catch(err => console.log(err));
  };

  return (
    <div className="container mt-4">
      <h2>Departments</h2>
      <AddDepartment refresh={fetchDepartments} />
      <table className="table table-bordered mt-3">
        <thead className="table-light">
          <tr>
            <th>ID</th>
            <th>Code</th>
            <th>Name</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {departments.map(dep => (
            <tr key={dep.id}>
              <td>{dep.id}</td>
              <td>{dep.code}</td>
              <td>{dep.name}</td>
              <td>
                <button className="btn btn-danger btn-sm" onClick={() => handleDelete(dep.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DepartmentList;
