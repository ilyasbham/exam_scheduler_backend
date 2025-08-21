from .models import Student
from department.models import Department

def create_student(data):
    student = Student.objects.create(**data)
    return student

def get_all_students():
    return Student.objects.all()

def get_student_by_id(student_id):
    return Student.objects.get(id=student_id)

def update_student(student_id, data):
    student = Student.objects.get(id=student_id)
    for key, value in data.items():
        setattr(student, key, value)
    student.save()
    return student

def delete_student(student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return True


