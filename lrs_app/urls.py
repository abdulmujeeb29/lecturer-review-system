from django.urls  import path 
from . import views 


urlpatterns = [
    path('student_register',views.student_register),
    path('student_login',views.student_login),
    path('regl',views.lecturer_register),
    path('logl',views.lecturer_login),
    path('index',views.index),
]

