from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import auth 
from django.contrib import messages 
from django.contrib.auth import authenticate,login 
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        username =request.POST['username']
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        email =request.POST['email']
        department = request.POST['department']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        user_type = request.POST['user_type']
        


        if password1== password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return render(request,'register.html')


            elif User.objects.filter(username=username).exists() :
                messages.info(request,'Username already used')
                return render(request,'register.html')

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
                user.first_name= firstname
                user.last_name = lastname
                user.user_type = user_type
                user.save();
                return redirect('/login')
            
        else:
            messages.info(request,'Passwords doesnt corresspond' )


    return render(request,'register.html')

def login(request):
    if request.method == 'POST' :


        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate( username=username, password=password1)

        if user is not None:
            if user.is_active:
                auth.login(request,user)
            
                if user.user_type == 'HOD': 
                    return redirect('/hod_dash')
            
                elif user.user_type == 'lecturer' :
                    return redirect('/lec_dash')
            

                elif user.user_type == 'student':
                    return redirect('/stu_dash')
            
            
                return render(request, 'index.html')
            else:
                messages.info(request,'Your account has been deactivated')

        else:
            messages.info(request,'Invalid credentials ')
            return redirect('/login')
    
    



    return render(request, 'login.html')


def index(request):
    return render(request,'index.html')

def student_dashboard(request):
    return render(request,'student_dashboard.html')

def lecturer_dashboard(request):
    return render(request,'lecturer_dashboard.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def update_lecturer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        specialization = request.POST['specialization']
        gender = request.POST['gender']


        lecturer = Lecturer(first_name=first_name, last_name=last_name, email=email,specialization=specialization)
        lecturer.gender=gender

        lecturer.save()

        return HttpResponse('Details updated successfully ') 
    
    else :

        return render(request,'update_lecturer.html')


def update_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        department = request.POST['department']
        gender = request.POST['gender']
        level = request.POST['level']


        student = Student(first_name=first_name, last_name=last_name, email=email,department=department)
        student.gender=gender
        student.level = level

        student.save()

        return HttpResponse('Details updated successfully ') 
    
    else:
        return render(request,'update_student.html')



def list_lecturer(request):
    lecturers = Lecturer.objects.all()
    return render(request,'list_lecturer.html', {'lecturers' : lecturers})


def list_student(request):
    students = Student.objects.all()
    return render( request,'list_student.html', {'students' : students})

from django.urls import reverse 
def detail_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':    
        student.is_active = not student.is_active 
        student.save()
        return redirect('detail_student', pk=pk)
    
    return render(request,'detail_student.html', {'student' : student})

from django.db.models import Q

def search_students(request):
    query = request.GET.get("search-query")
    if query:
        students = Student.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
    else:
        students = Student.objects.none()
    context = {'students': students, 'query': query}
    return render(request, 'search_results.html', context)



from django.db.models import Avg

def detail_lecturer(request, pk):
    lecturer = Lecturer.objects.get(id=pk)
    reviews = Review.objects.filter(lecturer=lecturer).order_by('created_at')
    

    num_reviews = reviews.count()
    avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

    
    if request.method =='POST':
        content= request.POST['content']
        rating = request.POST['rating']
        
        review = Review.objects.create( lecturer=lecturer ,content=content , rating =rating )
        review.save()


    

    return render(request,'detail_lecturer.html', {'lecturer' : lecturer , 'reviews': reviews , 'num_reviews' : num_reviews , 'avg_rating' : avg_rating }  )



def delete_student(request,pk):
    student=Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('detail_student', pk=pk)
    
    return render(request,'delete_student.html' ,{'student':student })

