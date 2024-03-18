from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    name=models.CharField(max_length=50,null=True)
    age = models.IntegerField(blank=True, null=True)
    subject=models.CharField(max_length=50)
    place=models.CharField(max_length=50,null=True)
