from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.student_exam_list_create, name='student-exam-list-create'),
    path('<int:pk>/', views.student_exam_detail, name='student-exam-detail'),
]
