from django.db import models
from exam.models import Exam
from research_assistant.models import ResearchAssistant



Exam_assignment_CHOICES = [
        ("main", "main"),
        ("backup", "backup"),
    ]

# Create your models here.
class Exam_assignment(models.Model):
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE,related_name="exam_assignments")
    research_assistant= models.ForeignKey(ResearchAssistant,on_delete=models.CASCADE,related_name="exam_assingnments")
    role=models.CharField(max_length=20,choices=Exam_assignment_CHOICES)
    
    
    def __str__(self):
      return f"Research Assistant {self.research_assistant} -> Exam {self.exam} -> Role {self.role}"
