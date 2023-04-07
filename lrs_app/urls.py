from django.urls  import path 
from . import views 


urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('student/dashboard',views.student_dashboard),
    path('lecturer/dashboard/<uuid:lecturer_id>/',views.lecturer_dashboard),
    path('admin_dashboard',views.admin_dashboard),
    path('update/lecturer', views.update_lecturer),
    path('list/lecturer',views.list_lecturer),
    path('profile/<str:pk>', views.detail_lecturer),
    path('update/student',views.update_student),
    path('list_student',views.list_student),
    path('search_students/',views.search_students , name='search_students'),
    path('detail/<int:pk>', views.detail_student , name='detail_student'),
    path('delete/<int:pk>', views.delete_student, name='delete_student'),
    path('',views.index),
    path('custom/page', views.custom_page),
    path('logout',views.logout),
    path('review/<uuid:pk>/update/', views.update_review, name='update_review'),
    path('review/<uuid:pk>/delete/', views.delete_review, name='delete_review'),
]

