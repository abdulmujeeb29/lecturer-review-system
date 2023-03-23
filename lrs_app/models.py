from django.db import models
from django.contrib.auth.models import UserManager, BaseUserManager, AbstractBaseUser

# class MyUserManager(UserManager):
#     pass


# Create your models here.

# class StudentManager(BaseUserManager):
#     def create_user(self, email, password1, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         #user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

class Admin(models.Model):
    name = models.CharField(max_length=5)
    

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
    level = models.CharField(max_length=5,choices=levels)

    # objects= StudentManager()

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'department']

    
    
    


    def __str__(self) -> str:
        return self.username



class Lecturer(models.Model):
    username = models.CharField(max_length=20)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email = models.EmailField(null=True)
    specialization = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20,choices=Gender,default='male')

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
    body = models.CharField(max_length=100, null= False, blank=False)
    rating= models.CharField(max_length=5,choices=Rating, default=1)
    lecturer_id = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)