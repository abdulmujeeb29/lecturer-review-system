from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect 
from django.urls import reverse 
from .models import *
from django.contrib.auth.models import auth 
from django.contrib import messages 
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# Create your views here.



def register(request):
    
    if request.method == 'POST':
        username =request.POST['username']
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        email =request.POST['email']
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
                if user_type == 'student':
                    student = Student.objects.create(
                        user=user,
                        department="",
                        level="",
                        matricno=""
                    )
                    student.save()
                elif user_type == 'lecturer':
                    lecturer = Lecturer.objects.create(
                        user=user,
                        specialization="",
                        phone_number=""
                    )
                    lecturer.save()
                user=authenticate(username=username, password=password1)


                if user is not None:
                    if user.is_active:

                   
                        auth.login(request,user)
            
                        if user.user_type == 'admin': 
                            return redirect('/admin_dashboard')
            
                        elif user.user_type == 'lecturer' :
                            return redirect('/lecturer/dashboard')
            

                        elif user.user_type == 'student':
                            return redirect('/student/dashboard')
                        
                    else:
                        messages.info(request,'Your account has been deactivated')

                else:
                    return render(request,'register.html')
        else:
            messages.info(request,'Passwords doesnt corresspond' )


    return render(request,'register.html')

def admin_register(request):
    if request.method == 'POST':
        username =request.POST['username']
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        user_type = request.POST['user_type']
        gender= request.POST['gender']
        


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
                user.gender = gender
                user.save();
                
                if user_type == 'admin':
                    Admin.objects.create(
                        user=user,
                        department=''
                    )
                
                user=authenticate(username=username, password=password1)

                if user is not None and user.is_active :
                    auth.login(request,user)
            
                    if user.user_type == 'admin': 
                        if user.is_active:

                            return redirect('/admin_dashboard')
                        else:
                            messages.error(request,'Your account has been deactivated')
                    
                else:
                    return render (request,'admin_register.html')
                
        else:
            messages.info(request,'Your passwords do not corespond ')


    return render (request,'admin_register.html')



def login(request):
    if request.method == 'POST' :


        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate( username=username, password=password1)

        if user is not None and  user.is_active:
            auth.login(request, user)

            if user.is_superuser or user.user_type == 'admin' :
                return redirect('/admin_dashboard')

            elif user.user_type == 'lecturer':
                if user.lecturer.is_active:
                    return redirect('/lecturer/dashboard')
                else:
                    messages.error(request, 'Your account has been deactivated')

            elif user.user_type == 'student':
                if user.student.is_active:
                    return redirect('/student/dashboard')
                else:
                    messages.error(request, 'Your account has been deactivated')

        else:
            messages.info(request,'Invalid credentials ')
            return redirect('/login')

    return render(request, 'login.html')


def logout(request):
    logout(request)
    redirect('/login')
    


def index(request):
    return render(request,'index.html')

@login_required
def student_dashboard(request):
    student = request.user.student  # Get the currently logged in student
    reviews =Review.objects.filter(student=student).order_by('-created_at')

    return render(request,'student_dashboard.html', {'reviews' : reviews})




@login_required
def update_review(request, pk):
    review = get_object_or_404(Review, pk=pk)      # accessing a review whose pk is a uuid , esy way using the get_obect_or_404


    if request.method == 'POST':
        review.content = request.POST['content']
        review.rating = request.POST['rating']
        review.save()
        return redirect('/student/dashboard')

    return render(request, 'update_review.html', {'review': review})

@login_required
def delete_review(request, pk):                    
    review = get_object_or_404(Review, pk=pk)      


    if request.method == 'POST':
        review.delete()
        return redirect('/student/dashboard')

    return render(request, 'delete_review.html', {'review': review})


def lecturer_dashboard(request):
    lecturer= request.user.lecturer
    reviews = Review.objects.filter(lecturer=lecturer)


    return render(request,'lecturer_dashboard.html', {'reviews':reviews})

def admin_dashboard(request):
    reviews = Review.objects.all()
    num_reviews = reviews.count()
    students=Student.objects.all()
    num_students= students.count()
    lecturers = Lecturer.objects.all()
    num_lecturers=lecturers.count()

    current_site = request.get_host()

    link = 'https://' + current_site + reverse('admin_register')

    return render(request,'admin_dashboard.html', {'num_reviews' : num_reviews , 'num_students' : num_students , 'num_lecturers' : num_lecturers , 'link' : link})



def update_admin(request):
    user = User.objects.get(id=request.user.id)
    try:
       admin = Admin.objects.get(user=request.user)
    except Admin.DoesNotExist:
        admin = None

    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.gender = request.POST['gender']
        user.save()

        if admin:
            admin.department = request.POST['department']
            admin.save()

        else:
            Admin.objects.create( user=request.user, department=request.POST['department'])
            
        return redirect('/update/admin')

    else:
        context= {
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'username': user.username,
            'department': admin.department if admin else '',
            'gender': user.gender 

        }

        return render (request,'update_admin.html' , context)
    

def update_lecturer(request):
    user = User.objects.get(id=request.user.id)
    try:
       lecturer = Lecturer.objects.get(user=request.user)
    except Lecturer.DoesNotExist:
        lecturer = None
        
    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.gender = request.POST['gender']
        user.save()
        
        if lecturer:
            lecturer.specialization = request.POST['specialization']
            lecturer.phone_number = request.POST['phone_number']
            lecturer.save()
        else:
            Lecturer.objects.create(
                user=request.user,
                specialization=request.POST['specialization'],
                phone_number=request.POST['phone_number'],
                
            )

        return redirect('/update/lecturer')
    
    else:
        context = {
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'username': user.username,
            'specialization': lecturer.specialization if lecturer else '',
            'phone_number': lecturer.phone_number if lecturer else '',
            
            'gender': user.gender
        }
        return render(request, 'update_lecturer.html', context)


def update_student(request):
    
    user = User.objects.get(id=request.user.id)
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
        
    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.gender = request.POST['gender']
        user.save()
        
        if student:
            student.department = request.POST['department']
            student.matricno = request.POST['matricno']
            student.level = request.POST['level']
            student.save()
        else:
            Student.objects.create(
                user=request.user,
                department=request.POST['department'],
                matricno=request.POST['matricno'],
                level=request.POST['level']
            )

        return redirect('/update/student')
    
    else:
        context = {
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'username': user.username,
            'department': student.department if student else '',
            'matricno': student.matricno if student else '',
            'level': student.level if student else '',
            'gender': user.gender 
        }
        return render(request, 'update_student.html', context)

def admin_lecturer_list(request):
    lecturers=Lecturer.objects.all()
    return render (request,'admin_lecturer_list.html', {'lecturers' : lecturers})

def list_lecturer(request):
    lecturers = Lecturer.objects.select_related('user').all()
    return render(request,'list_lecturer.html', {'lecturers' : lecturers})


def list_student(request):
    students = Student.objects.all()
    return render( request,'list_student.html', {'students' : students})



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
@login_required
def detail_lecturer(request, pk):
    lecturer = Lecturer.objects.get(id=pk)
    reviews = Review.objects.filter(lecturer=lecturer).order_by('created_at')
    

    num_reviews = reviews.count()
    avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    # avg_rating =  round(avg_rating, 2)                               
    student = Student.objects.get(user=request.user)            
        
    
    if request.method =='POST':
        content= request.POST['content']
        rating = request.POST['rating']
        
        review = Review.objects.create(student=student , lecturer=lecturer , content=content , rating =rating  )
        review.save()


    

    return render(request,'detail_lecturer.html', {'lecturer' : lecturer , 'reviews': reviews , 'num_reviews' : num_reviews , 'avg_rating' : avg_rating , 'student' : student}  )


#  admin priviledges 

def delete_student(request,pk):
    student=get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('/admin_list/student', pk=pk)
    
    return render(request,'delete_student.html' ,{'student':student })

def delete_lecturer(request,pk):
    lecturer =get_object_or_404(Lecturer, pk=pk)
    if request.method =='POST':
        lecturer.delete()
        return redirect('/admin_list/lecturer', pk=pk)
    
    return render(request,'delete_lecturer.html', {'lecturer' : lecturer})

from django.urls import reverse 

def activate_student(request, pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.is_active = not student.is_active
        student.save()
        return redirect('/admin_list/student', pk=pk)
    
    return render(request, 'deactivate_student.html', {'student': student})

def activate_lecturer(request,pk):
    lecturer= get_object_or_404(Lecturer,pk=pk)
    if request.method =='POST':
        lecturer.is_active = not lecturer.is_active
        lecturer.save()
        return redirect('/admin_list/lecturer', pk=pk)
    
    return render (request,'activate_lecturer.html', {'lecturer' : lecturer })


def custom_page(request):
    return render (request,'custom_page.html')