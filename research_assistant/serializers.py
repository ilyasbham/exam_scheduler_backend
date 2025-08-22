from rest_framework import serializers
from .models import ResearchAssistant
from department.models import Department

class ResearchAssistantSerializer(serializers.ModelSerializer):
    # For read: nested string
    department = serializers.StringRelatedField(read_only=True)

    # For write: use department_id
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',  # maps to FK
        write_only=True
    )

    class Meta:
        model = ResearchAssistant
        fields = ['assistant_id', 'name', 'email', 'phone_no', 'address', 'department', 'department_id']
