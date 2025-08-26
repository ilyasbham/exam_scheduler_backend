from django.contrib import admin
from .models import Classroom

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('id', 'capacity', 'availability')
    list_filter = ('availability',)
    search_fields = ('id',)
