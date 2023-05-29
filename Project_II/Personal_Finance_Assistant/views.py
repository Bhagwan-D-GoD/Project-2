from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.

def index(request):
    return(render(request,"index.html"))

def register(request):
    if request.method == 'POST':
        try:
            name = request.POST.get("name")
            user_id = request.POST.get("user_id")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password != confirm_password:
                print("Password does not match")
                messages.error(request,"Password does not match")
                return(redirect('index'))
            #to check if the user_id already exists or not 
            #if User_Info.objects.filter(user_id=u_id).exists():
                #User.objects.filter(username=self.cleaned_data['username']).exists():
                #messages.error(request,"user already exists")
                #return render(request, 'login.html') 
         
                #messages.success(request, 'Account created succesfully. Now you can login.')
                #return render(request, 'login.html')
        except IndexError:
            #This means that the face_recognition module couldn't find any faces i
        
            messages.error(request,"face is not detected in the provided image please provide correct image")
            return redirect("index")
    return(render(request,"index.html"))

def login(request):
    if request.method =="POST":
        messages.error(request,"Password does not match")
        return(redirect('index'))