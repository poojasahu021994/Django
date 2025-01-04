from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def data(request):
    print(request.methode)
    print(request.FILES)
    print(request.POST)
