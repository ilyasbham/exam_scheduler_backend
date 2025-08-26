from django.db import models

# Create your models here.


Department_CHOICES = [
        ("Compute Engineering", "Computer Engineering"),
        ("Electronic Engineering", "Electronic Engineering"),
    ]

class Department(models.Model):
  
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100,choices=Department_CHOICES)

    def __str__(self):
        return f"{self.code} - {self.name}"
