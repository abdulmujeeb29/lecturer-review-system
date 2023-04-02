from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    user_type_data = (('HOD','HOD') , ('lecturer', 'lecturer') , ('student', 'student'))
    user_type = models.CharField(max_length=10, choices=user_type_data, default='HOD')
    is_active= models.BooleanField(default=True)
    # gender_data =(('male','male') , ('female', 'female') ,('others', 'others') )
    # gender = models.CharField(max_length=10, choices=gender_data , null=True)
    
class Admin(models.Model):
    name = models.CharField(max_length=5)
    email = models.EmailField(null=True )
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
    username = models.CharField(max_length=20)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    level = models.CharField(max_length=5)
    gender =models.CharField(max_length=6, null=True)
    is_active= models.BooleanField(default=True)
    
    #admin_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    
    


    def __str__(self) -> str:
        return self.username


def max_length(value):
    if len(value) > 11 :
        return ValidationError('invalid Phonenumber ')


class Lecturer(models.Model):
    username = models.CharField(max_length=20)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email = models.EmailField(null=True)
    specialization = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, null=True)
    phone_number = models.IntegerField(validators=[max_length],null=True, blank=True)

    #admin_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)

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
    content= models.CharField(max_length=100, null= False, blank=False)
    rating= models.IntegerField()
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[:50]