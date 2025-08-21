from .models import Department

def create_department(data):
    department = Department.objects.create(**data)
    return department

def get_all_departments():
    return Department.objects.all()

def get_department_by_id(dept_id):
    return Department.objects.get(id=dept_id)

def update_department(dept_id, data):
    dept = Department.objects.get(id=dept_id)
    for key, value in data.items():
        setattr(dept, key, value)
    dept.save()
    return dept

def delete_department(dept_id):
    dept = Department.objects.get(id=dept_id)
    dept.delete()
    return True