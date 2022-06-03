from django.db import models
from django.contrib.auth.models import (AbstractBaseUser ,BaseUserManager ,PermissionsMixin)

# Create your models here.

class UserAccountMagaer(BaseUserManager):
    def create_superuser(self, username, password, first_name, last_name, **other_fields):
        other_fields.setdefault('admin', True)
        other_fields.setdefault('annotatorRole', True)
        other_fields.setdefault('modelBuilderRole', True)
        other_fields.setdefault('analystRole', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('admin') is not True:
            raise ValueError('Superuser must be assigned to admin=True.')

        return self.create_user(username, first_name, last_name, password, **other_fields)

    def create_user(self, username, first_name, last_name, password, **other_fields):

        if not username:
            raise ValueError(('You must provide a username'))

        user = self.model(username=username, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=False)
    first_name = models.CharField(max_length=255, unique=False, blank=True)
    last_name = models.CharField(max_length=255, unique=False, blank=True)
    
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default = False)
    annotatorRole = models.BooleanField(default = False)
    modelBuilderRole = models.BooleanField(default = False)
    analystRole = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)

    objects  = UserAccountMagaer()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.username
