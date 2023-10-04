from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .form import SignUpForm
from.models import User_Info
# Create your views here.


def signin(request):
        try:
            form = SignUpForm()
            if request.method == "POST":
                form = SignUpForm(request.POST)   
                if form.is_valid():
                    form.save()
                    messages.success(request,"Account created sucessfully!")
                    return redirect("index")
                
            context = {'form':form}
            return render(request,'index.html',context)
        except IndexError:
            return redirect("index")

def log_in(request):
    try:
        if request.method =="POST":
            u_id = request.POST.get("username")
            pass_word = request.POST.get("password1")
            user = authenticate(request, username=u_id, password=pass_word)
        if user is not None:
            request.session['session_username']=u_id
            login(request, user)
            return redirect('landing')  # Change 'home' to the appropriate URL name
        messages.error(request,"Invalid Username or Password")
        return(redirect('index'))
    except:
        return redirect('index')


def landing(request):
    if request.session.has_key('session_username'):
        return render(request,'landingpage.html')
    else:
        return redirect('login')

def navbar(request):
    return render(request,'reusablenavbar.html')
    
   