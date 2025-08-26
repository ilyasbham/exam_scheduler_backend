from django.contrib import admin

# Register your models here.
from .models import StudentExam

@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'exam')
    list_filter = ('exam', 'student')
