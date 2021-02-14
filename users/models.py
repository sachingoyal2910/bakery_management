from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=False, unique=True)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)
    address = models.CharField(verbose_name="Address", help_text="Address of Customer", null=False, max_length=255, blank=False)
