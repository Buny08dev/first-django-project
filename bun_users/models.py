from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
# Create your models here.
# from django.contrib.auth.models import AnonymousUser

class UserMod(AbstractUser):
    image=models.ImageField(upload_to='profile',blank=True,null=True,verbose_name='avatar')   
    phone = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Telefon raqam"
    )
    def __str__(self):
        return self.username
    
    class Meta:
        db_table="Users"
        verbose_name="User"
        verbose_name_plural="Userlar"
