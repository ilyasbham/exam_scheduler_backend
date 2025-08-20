from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .services import create_student, get_all_students

@api_view(['GET'])
def list_students(request):
    students = get_all_students()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    student = create_student(request.data)
    serializer = StudentSerializer(student)
    return Response(serializer.data)
