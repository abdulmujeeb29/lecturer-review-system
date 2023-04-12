from django.urls  import path 
from . import views 


urlpatterns = [
    path('register',views.register),
    path('admin_register', views.admin_register, name="admin_register"),
    path('login',views.login),
    path('student/dashboard',views.student_dashboard),
    path('lecturer/dashboard',views.lecturer_dashboard),
    path('admin_dashboard',views.admin_dashboard),
    path('update/admin',views.update_admin),
    path('update/lecturer', views.update_lecturer),
    path('list/lecturer',views.list_lecturer),
    path('profile/<uuid:pk>', views.detail_lecturer),
    path('update/student',views.update_student),
    path('admin_list/student',views.list_student),
    path('admin_list/lecturer', views.admin_lecturer_list),
    path('search_students/',views.search_students , name='search_students'),
    path('student/<uuid:pk>/activate/', views.activate_student , name='activate_student'),
    path('lecturer/<uuid:pk>/activate/', views.activate_lecturer , name='activate_lecturer'),
    path('student/<uuid:pk>/delete/', views.delete_student, name='delete_student'),
    path('lecturer/<uuid:pk>/delete/', views.delete_lecturer, name='delete_lecturer'),
    path('',views.index),
    path('custom/page', views.custom_page),
    path('logout',views.logout),
    path('review/<uuid:pk>/update/', views.update_review, name='update_review'),
    path('review/<uuid:pk>/delete/', views.delete_review, name='delete_review'),
]

