# courses/models.py

from django.db import models
from departments.models import Department

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
