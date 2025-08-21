from rest_framework import serializers
from .models import Student
from department.models import Department

class StudentSerializer(serializers.ModelSerializer):
    # read nested department name
    department = serializers.StringRelatedField(read_only=True)

    # write by department id
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',  # maps to model FK
        write_only=True
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'department', 'department_id', 'year', 'age', 'phone', 'email', 'address']
