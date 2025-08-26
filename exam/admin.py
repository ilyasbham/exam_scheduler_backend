from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'exam_date', 'start_time', 'end_time', 'classroom')
    list_filter = ('exam_date', 'course', 'classroom')
    search_fields = ('course__name',)
