# from django.contrib.auth.models import User as AuthUser

# # Create your models here.

# # college_app/models.py

# from django.contrib.auth.models import User as AuthUser



# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField()
#     auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)



# # class ContactUs(models.Model):
# #     user_email = models.EmailField(default = "asda@dssd.com")
# #     name = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     message = models.TextField()

# class ContactUs(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()

#     def __str__(self):
#         return self.name



from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class FormData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.field1} - {self.field2} - {self.field3}'