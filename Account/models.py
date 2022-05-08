from email.headerregistry import Address
from unicodedata import name
from django.db import models
from typing import final
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is requeired')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', "admin")

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self._create_(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    is_teacher = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

    
class Jwt(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name='login_user', on_delete=models.CASCADE
    )
    access = models.TextField()
    refresh = models.TextField()
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlackListedToken(models.Model):
    refresh = models.TextField()

class Teacher(models.Model):
    gender = (('male', 'M'),
            ('Female', 'F')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    Surname = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    Gender = models.CharField(choices=gender, max_length=30)
    Address = models.CharField(max_length=100)
    Date_of_birth = models.DateField()
    state_of_residence = models.CharField(max_length=40)
    verified = models.BooleanField(default=False)
    disability = models.BooleanField(default=False)
    About_Teacher = models.TextField()
    Facebook = models.CharField(max_length=100)
    Twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    @final 
    def __str__(self):
        return self.first_name


class TeachersBankDetails(models.Model):
    user = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    bank_acount_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=20)
    account_number = models.IntegerField()