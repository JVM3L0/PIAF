from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    complete_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=11, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]
    objects = AccountManager()

class Dependent(models.Model):
    complete_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    guardian = models.ForeignKey(Account, on_delete=models.CASCADE)
