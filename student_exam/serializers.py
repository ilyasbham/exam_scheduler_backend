from rest_framework import serializers
from .models import StudentExam

class StudentExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExam
        fields = '__all__'
