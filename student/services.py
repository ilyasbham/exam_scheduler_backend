from .models import Student

def create_student(data):
    student = Student.objects.create(**data)
    return student

def get_all_students():
    return Student.objects.all()
