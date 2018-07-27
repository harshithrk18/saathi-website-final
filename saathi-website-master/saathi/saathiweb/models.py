from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    message = models.TextField()



