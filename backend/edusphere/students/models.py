from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=128, default='your_default_password_here')  # Define a default value

    def __str__(self):
        return self.name
