from django.db import models
from department.models import Department

class ResearchAssistant(models.Model):
    assistant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name="assistants"
    )
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
