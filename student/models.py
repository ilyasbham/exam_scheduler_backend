from django.db import models

# Create your models here.

class Student(models.Model):
    name       = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year       = models.IntegerField()
    age        = models.IntegerField()
    phone      = models.CharField(max_length=20)
    email      = models.EmailField()
    address    = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
