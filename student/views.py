# from django.shortcuts import render

# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import StudentSerializer
# from .services import create_student, get_all_students

# @api_view(['GET'])
# def list_students(request):
#     students = get_all_students()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_student(request):
#     student = create_student(request.data)
#     serializer = StudentSerializer(student)
#     return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .services import create_student, get_all_students, get_student_by_id, update_student, delete_student

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

@api_view(['GET'])
def get_student(request, student_id):
    student = get_student_by_id(student_id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_student(request, student_id):
    student = update_student(student_id, request.data)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['DELETE'])
def remove_student(request, student_id):
    delete_student(student_id)
    return Response({"message": "Student deleted successfully"})
