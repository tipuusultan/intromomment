from django.db import models
from datetime import date,timedelta
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.conf import settings



class MyAccuntManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Please enter an email address")
        if not username:
            raise ValueError("Please enter a username")
        user= self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )    
        user.is_admin =True
        user.is_staff =True
        user.is_superuser =True
        user.is_active=True
        user.save(using=self._db)
        return user




class accounts(AbstractUser):
    email           =   models.EmailField(verbose_name="email",max_length=100,unique=True)
    username        =   models.CharField(max_length=40, unique=False, default='')
    date_joined     =   models.DateField(auto_now_add=True)
    otp             =   models.IntegerField(default=0)
    is_admin        =   models.BooleanField(default=False)
    is_active       =   models.BooleanField(default=False)
    is_staff        =   models.BooleanField(default=False)
    is_superuser    =   models.BooleanField(default=False)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    objects=MyAccuntManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin    
    def has_module_perms(self, app_label):
        return True    