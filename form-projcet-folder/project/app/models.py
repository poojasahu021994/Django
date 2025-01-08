from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    detail=models.CharField(max_length=100)
    phone=models.IntegerField()
    volume=models.IntegerField()
    subscribe =models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    password=models.CharField(max_length=16)
    profile_pic=models.ImageField()
    resume=models.FileField()