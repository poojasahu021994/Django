from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    detail=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    volume=models.IntegerChoices()
    subscribe=models.Choices()
    gender=models.Choices()
    dob=models.IntegerField()
    password=models.CharField(max_length=16)
    cpassword=models.CharField(max_length=16)
    profile_pic=models.FilePathField()
    resume=models.FilePathField()