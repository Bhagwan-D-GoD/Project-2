from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .form import SignUpForm,TransactionForm
from .models import IncomeRecord

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
            login(request, user)
            request.session['username'] = u_id #setting the session variable
            return redirect('landing')  # Change 'home' to the appropriate URL name
        messages.error(request,"Invalid Username or Password")
        return(redirect('index'))
    except:
        return redirect('index')


def landing(request):
    return render(request,'landingpage.html')

def navbar(request):
    return render(request,'reusablenavbar.html')
    
def income_expenses(request):
    try:
            #print(request.session.get('username'))
            uname =  request.session.get('username')
            form = TransactionForm
            if request.method == "POST":
                form = TransactionForm(request.POST)   
                if form.is_valid():
                    incomerecord = IncomeRecord()
                    incomerecord.user = User.objects.get(username=uname)
                    incomerecord.category = form.cleaned_data['category']
                    incomerecord.title = form.cleaned_data['title']
                    incomerecord.amount = form.cleaned_data['amount']
                    incomerecord.finance = form.cleaned_data['finance_type']
                    incomerecord.save()
                    messages.success(request,"Data Stored sucessfully!")
                    return redirect("income_expenses")
            #for transfering income expense form and icome expense data to template
           # print(request.session.get('username'))
            user_instance = User.objects.get(username=uname)
            
            income_data = IncomeRecord.objects.filter(user=user_instance) #to get the user instance
            print(income_data)
            context = {'form':form,
                       'income_data':income_data}
            return render(request,'income_expenses.html',context)
    except IndexError:
            return redirect("index")
    