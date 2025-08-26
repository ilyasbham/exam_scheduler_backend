from django.urls import path
from . import views

urlpatterns = [
    path('exams/', views.exam_list_create, name='exam-list-create'),
    path('exams/<int:pk>/', views.exam_detail, name='exam-detail'),
]
