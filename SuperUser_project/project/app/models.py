from django.db import models

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, help_text="Enter your name")
    email=models.EmailField(help_text="Enter Email", unique=True)
    emp_joing_date =models.DateTimeField(auto_now_add=True)
    emp_updated_at=models.DateTimeField(auto_now=True)
    detail=models.CharField(max_length=100, help_text="Enter your details")
    phone=models.IntegerField(help_text="Enter your number")
    emp_start_time=models.TimeField()
    gender=models.Choices(max_length=10)
    emp_dob=models.DateTimeField()
    emp_active=models.BooleanField()
    password=models.CharField(max_length=16)
    profile_pic=models.ImageField(upload_to='image/')
    resume=models.FileField(upload_to='file/')
# Create your models here.
