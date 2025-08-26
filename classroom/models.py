from django.db import models

class Classroom(models.Model):
    capacity = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        status = "Available" if self.availability else "Unavailable"
        return f"Classroom {self.id} - Capacity: {self.capacity} ({status})"
