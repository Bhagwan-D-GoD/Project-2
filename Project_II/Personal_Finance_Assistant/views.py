from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate 
from.models import User_Info
# Create your views here.

def index(request):
    return(render(request,"index.html"))

def register(request):
    if request.method == 'POST':
        try:
            name = request.POST.get("name")
            u_id = request.POST.get("user_id")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if User_Info.objects.filter(user_id=u_id).exists():
                messages.error(request,"user already exists")
                return redirect('index') 
            if password != confirm_password:
                print("Password does not match")
                messages.error(request,"Password does not match")
                return(redirect('index'))
            password = make_password(password) #to encrpt the password 
            newaccount = User_Info()
            newaccount.user_name = name
            newaccount.user_id = u_id
            newaccount.password = password
            newaccount.email = email
            newaccount.save()
            messages.success(request,"Account created sucessfully!")
        except IndexError:
            return redirect("index")
    return(render(request,"index.html"))

def login(request):
    try:
        if request.method =="POST":
            u_id = request.POST.get("user_id")
            pass_word = request.POST.get("password")
            if User_Info.objects.filter(user_id=u_id).exists():
                user = User_Info.objects.get(user_id=u_id)
                if check_password(pass_word,user.password):#compares plain password and hashed password
                    return(HttpResponse('welcome to our site'))
            messages.error(request,"Invalid Username or Password")
            return(redirect('index'))
    except:
        return redirect(index)