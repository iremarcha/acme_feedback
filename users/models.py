from django.db import models

from PIL import Image
from django.contrib.auth.base_user import BaseUserManager
from phone_field import PhoneField
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, uvus, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("Enter a valid email.")
        if not uvus:
            raise ValueError("Enter a valid uvus.")
        if not password:
            raise ValueError("Enter a valid password.")
        
        user = self.model(
         	uvus = uvus,
            email = self.normalize_email(email))

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, uvus, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(uvus, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    uvus = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25, unique=False)
    surname = models.CharField(max_length=25, unique=False)
    role = models.CharField(max_length=50, unique=False)
    email = models.EmailField(unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #phone = PhoneField(blank=True, help_text='Contact phone number')
    
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "uvus"
    REQUIRED_FIELDS = ["email"]
    def __str__(self):
        return self.uvus
