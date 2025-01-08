from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def new1(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)

    name=request.POST.get('fname')
    image=request.POST.get('image')
    print(name,image)
