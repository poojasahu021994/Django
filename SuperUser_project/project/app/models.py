from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50, help_text="Enter your name")
    email=models.EmailField(help_text="Enter Email")
    detail=models.CharField(max_length=100, help_text="Enter your details")
    phone=models.IntegerField(help_text="Enter your number")
    volume=models.IntegerField()
    subscribe =models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    password=models.CharField(max_length=16)
    profile_pic=models.ImageField()
    resume=models.FileField()
# Create your models here.
