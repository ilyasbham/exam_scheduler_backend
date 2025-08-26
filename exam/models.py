from django.db import models
from course.models import Course
from classroom.models import Classroom

# Create your models here.

class Exam(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='exams')
    exam_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE,related_name='exams')
    
    class Meta:
        ordering = ['exam_date', 'start_time']

    def __str__(self):
        return f"{self.course.name} — {self.exam_date} {self.start_time}-{self.end_time}"