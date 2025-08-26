from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StudentExam
from .serializers import StudentExamSerializer

@api_view(['GET', 'POST'])
def student_exam_list_create(request):
    if request.method == 'GET':
        student_exams = StudentExam.objects.all()
        serializer = StudentExamSerializer(student_exams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_exam_detail(request, pk):
    try:
        student_exam = StudentExam.objects.get(pk=pk)
    except StudentExam.DoesNotExist:
        return Response({"error": "StudentExam not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentExamSerializer(student_exam)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentExamSerializer(student_exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_exam.delete()
        return Response({"message": "StudentExam deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
