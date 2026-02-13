from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserMod(AbstractUser):
    image=models.ImageField(upload_to='profile',blank=True,null=True,verbose_name='avatar')
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table="Users"
        verbose_name="User"
        verbose_name_plural="Userlar"