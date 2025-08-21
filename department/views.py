# Create your views here.
#this is controller

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DepartmentSerializer
from .services import create_department, get_all_departments, get_department_by_id, update_department, delete_department

@api_view(['GET'])
def list_departments(request):
    departments = get_all_departments()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_department(request):
    department = create_department(request.data)
    serializer = DepartmentSerializer(department)
    return Response(serializer.data)

@api_view(['GET'])
def get_department(request, dept_id):
    dept = get_department_by_id(dept_id)
    serializer = DepartmentSerializer(dept)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_department(request, dept_id):
    dept = update_department(dept_id, request.data)
    serializer = DepartmentSerializer(dept)
    return Response(serializer.data)

@api_view(['DELETE'])
def remove_department(request, dept_id):
    delete_department(dept_id)
    return Response({"message": "Department deleted successfully"})