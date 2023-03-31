from django.urls  import path 
from . import views 


urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('index',views.index),
    path('stu_dash',views.student_dashboard),
    path('lec_dash',views.lecturer_dashboard),
    path('hod_dash',views.admin_dashboard),
    path('update_lecturer', views.update_lecturer),
    path('list_lecturer',views.list_lecturer),
    path('profile/<str:pk>', views.detail_lecturer),
    path('update_student',views.update_student),
    path('list_student',views.list_student),
    path('search_students/',views.search_students , name='search_students'),
    
]

