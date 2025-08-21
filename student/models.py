from django.db import models
from department.models import Department

from department.models import Department

class Student(models.Model):
    name       = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year       = models.IntegerField()
    age        = models.IntegerField()
    phone      = models.CharField(max_length=20)
    email      = models.EmailField()
    address    = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



