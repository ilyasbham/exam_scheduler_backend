import React from "react";
import { Card, Row, Col } from "react-bootstrap";

function StudentList({ students }) {
  return (
    <Row className="mt-4">
      {students.map((student) => (
        <Col key={student.id} md={6} lg={4} className="mb-3">
          <Card className="shadow-sm">
            <Card.Body>
              <Card.Title>{student.name}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">{student.department}</Card.Subtitle>
              <Card.Text>
                Year: {student.year} <br />
                Age: {student.age} <br />
                Phone: {student.phone} <br />
                Email: {student.email} <br />
                Address: {student.address}
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
}

export default StudentList;
