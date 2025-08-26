# Register your models here.
from django.contrib import admin
from .models import Course

# Register your models here.





@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name', 'department__name')
