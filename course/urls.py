from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.course_list_create, name='course_add'),
]

