from rest_framework import serializers
from .models import Course
from department.models import Department

class CourseSerializer(serializers.ModelSerializer):
    # Read department as name
    department = serializers.StringRelatedField(read_only=True)
    # Write using department id
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'department', 'department_id']



