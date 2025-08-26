from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_students),
    path('add/', views.add_student),
    path('<int:student_id>/', views.get_student),
    path('<int:student_id>/edit/', views.edit_student),
    path('<int:student_id>/delete/', views.remove_student),
]
