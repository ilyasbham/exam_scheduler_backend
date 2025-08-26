from django.db import models

class Classroom(models.Model):
    code = models.CharField(max_length=20, unique=True)  # new attribute
    capacity = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        status = "Available" if self.availability else "Unavailable"
        return f"Classroom {self.code} - Capacity: {self.capacity} ({status})"
