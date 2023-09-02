from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10)

    # Additional fields or methods can be added as needed

    def __str__(self):
        return self.name