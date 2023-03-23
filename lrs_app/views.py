from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User,auth 
from django.contrib import messages 
from django.contrib.auth import authenticate,login 
# Create your views here.

def student_register(request):
    
    if request.method == 'POST':
        username =request.POST['username']
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        email =request.POST['email']
        department = request.POST['department']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        


        if password1== password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return render(request,'student_register.html')


            elif User.objects.filter(username=username).exists() :
                messages.info(request,'Username already used')
                return render(request,'student_register.html')

            elif len(username) >10 :
                messages.info(request,'username must be less than 10 characters ')

            elif not username.isalnum():
                messages.info(request,' Username should be Alphanumeric characters only ')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    
                )
                user.save();
                return redirect('/student_login')
            
        else:
            messages.info(request,'Passwords doesnt corresspond' )


    return render(request,'student_register.html')

def student_login(request):
    if request.method == 'POST' :


        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate( username=username, password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'Invalid credentials ')
            return redirect('/student_login')
    

    return render(request, 'student_login.html')

def lecturer_register(request):
    return render(request,'lecturer/register.html')

def lecturer_login(request):
    return render(request,'lecturer/login.html')

def index(request):
    return render(request,'index.html')