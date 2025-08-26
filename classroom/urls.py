from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.classroom_list_create, name='classroom_add'),
]
