# users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """Create and return a superuser with an email, name, and password."""
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.is_staff = True  # Ensure is_staff is set for superuser
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Added is_staff field
    is_active = models.BooleanField(default=True)  # Added is_active field

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
