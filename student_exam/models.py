from django.db import models
from student.models import Student
from exam.models import Exam

# Create your models here.
class StudentExam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_exams')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student_exams')

    class Meta:
        unique_together = (('student', 'exam'),)  # prevent duplicates
        ordering = ['exam']
    
    def __str__(self):
        return f"Student {self.student.id} -> Exam {self.exam.id}"
