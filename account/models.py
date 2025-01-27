from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    complete_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=11, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"

    objects = AccountManager()

    def __str__():
        return self.email


class Dependent(models.Model):
    complete_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    guardian = models.ForeignKey(Account, on_delete=models.CASCADE)
