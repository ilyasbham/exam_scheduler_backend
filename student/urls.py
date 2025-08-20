from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_students),
    path('add/', views.add_student),
]
