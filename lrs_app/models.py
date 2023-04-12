import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    user_type_data = (('admin','admin') , ('lecturer', 'lecturer') , ('student', 'student'))
    user_type = models.CharField(max_length=10, choices=user_type_data, default='admin')
    is_active= models.BooleanField(default=True)
    gender_data = (('male','male') , ('female', 'female') , ('other', 'other'))
    gender = models.CharField(max_length=10, choices=gender_data)

    
class Admin(models.Model):
    department = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    is_active= models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

levels = (
    ('100l','100l'),
    ('200l','200l'),
    ('300l', '300l'),
    ('400l', '400l'),
    ('500l', '500l')

    )

Gender = (
    ('male','male'),
    ('female','female'),
    ('others','others')
)

class Student(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)           
    #The OneToOneField creates a unique relationship between the two models, where a Student object can only have one associated CustomUser
    department = models.CharField(max_length=20)
    level = models.CharField(max_length=5)
    matricno = models.CharField(max_length=10,null=True)
    is_active= models.BooleanField(default=True)
    
  
    

    def __str__(self) -> str:
        return self.username


def max_length(value):
    if len(value) > 11 :
        return ValidationError('invalid Phonenumber ')


class Lecturer(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    #The OneToOneField creates a unique relationship between the two models, where a Student object can only have one associated CustomUser
    specialization = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, null=True)
    is_active= models.BooleanField(default=True)

   
    def __str__(self) -> str:
        return self.username


Rating = (
    ('1', '1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),

)



class Review(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    content= models.CharField(max_length=100, null= False, blank=False)
    rating= models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.body[:50]
   