import React, { useState } from "react";
import AddStudent from "./components/AddStudent";
import StudentList from "./components/StudentList";
import AddDepartment from "./components/AddDepartment";
import DepartmentList from "./components/DepartmentList";
import { Container, Button, ButtonGroup } from "react-bootstrap";

function App() {
  const [students, setStudents] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [activeTab, setActiveTab] = useState("students"); // 'students' or 'departments'

  // Student handlers
  const handleAddStudent = (student) => {
    setStudents([...students, student]);
  };

  // Department handlers
  const handleAddDepartment = (department) => {
    setDepartments([...departments, department]);
  };

  return (
    <Container className="mt-4">
      <h1 className="text-center mb-4">🏫 School Management</h1>

      <ButtonGroup className="mb-4">
        <Button
          variant={activeTab === "students" ? "primary" : "outline-primary"}
          onClick={() => setActiveTab("students")}
        >
          Students
        </Button>
        <Button
          variant={activeTab === "departments" ? "primary" : "outline-primary"}
          onClick={() => setActiveTab("departments")}
        >
          Departments
        </Button>
      </ButtonGroup>

      {activeTab === "students" && (
        <>
          <AddStudent onAdd={handleAddStudent} />
          <StudentList students={students} />
        </>
      )}

      {activeTab === "departments" && (
        <>
          <AddDepartment onAdd={handleAddDepartment} />
          <DepartmentList departments={departments} />
        </>
      )}
    </Container>
  );
}

export default App;
