from django.shortcuts import render
from .forms import Emp_Form

def Empform(request):
    form =Emp_Form()
    return render(request,'home.html',{'form':form})
