from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def data(request):
    print(request.method)
    print(request.FILES)
    print(request.POST)

    name = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    age = request.POST.get('age')
    volume = request.POST.get('volume')
    subscribe = request.POST.getlist('subscribe')
    gender = request.POST.get('gender')
    dob = request.POST.get('dob')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    profile_pic = request.FILES.get('profile-pic')
    resume = request.FILES.get('resume')

    print(name)
    print(email)
    print(detail)
    print(phone)
    print(age)
    print(volume)
    print(subscribe)
    print(gender)
    print(dob)
    print(profile_pic)
    print(resume)
    print(password)
    print(cpassword)

    # print(name,email,detail,phone,age,volume,subscribe,gender,dob,password,cpassword,profile_pic,resume)

   

    # user_data={
    #     'name' : name,
    #     'email': email,
    #     'detail': detail,
    #     'phone': phone,
    #     'age': age,
    #     'volume': volume,
    #     'subscribe': subscribe,
    #     'gender': gender,
    #     'dob': dob,
    #     'profile_pic': profile_pic,
    #     'resume': resume,
    #     'password': password,
    #     'cpassword': cpassword
    # }
    # print(user_data)

    # user_data = {
    #     'name' : request.POST.get('username'),
    #     'email': request.POST.get('email'),
    #     'detail': request.POST.get('detail'),
    #     'phone': request.POST.get('phone'),
    #     'age': request.POST.get('age'),
    #     'volume': request.POST.get('volume'),
    #     'subscribe': request.POST.get('subscribe'),
    #     'gender': request.POST.get('gender'),
    #     'dob': request.POST.get('dob'),
    #     'profile_pic': request.FILES.get('profile-pic'),
    #     'resume': request.FILES.get('resume'),
    #     'password': request.POST.get('password'),
    #     'cpassword': request.POST.get('cpassword')
    #    }
    # print(user_data)

    # for i,j in request.POST.items():
    #     print(i,j)

    # for i in request.POST.keys():
    #     print(i)

    # for i in request.POST.values():
    #     print(i)

    # return render(request,'home.html',{'user_data':user_data})



    

