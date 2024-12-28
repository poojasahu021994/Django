from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(requset):

    return HttpResponse('<h1 style="background-color: yellow; color: red; margin: 400px;" >hello</h1>')