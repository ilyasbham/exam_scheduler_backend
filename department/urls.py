from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_departments),
    path('add/', views.add_department),
    path('<int:dept_id>/', views.get_department),
    path('<int:dept_id>/edit/', views.edit_department),
    path('<int:dept_id>/delete/', views.remove_department),
]