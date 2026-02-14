from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from bun_users.models import UserMod
from django import forms
import re
from django.core.exceptions import ValidationError
# from django.contrib.auth.validators import UnicodeUsernameValidator


class LoginForm(AuthenticationForm):
    use_required_attribute= False
    
    username = forms.CharField(
        label="Ism", # 'Username' o'rniga 'Ism' chiqadi
        required=True,
        widget=forms.TextInput(attrs={
            'class': "auth-form-group", # CSS klasslar bo'lsa shu yerga qo'shing
            'placeholder': 'Foydalanuvchi nomi',
            'required': False ,
        }),
        error_messages={"required":"bosh bolmasin"}

    )
    password = forms.CharField(
        label="Parol", # 'Password' o'rniga 'Parol' chiqadi
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'auth-form-group',
            'placeholder': 'Parol',
            'required': False ,
        }),
        error_messages={"required":"bosh bolmasin"}
    )
    error_messages = {
        'invalid_login': "Ism yoki parol xato kiritildi. Iltimos, qaytadan tekshiring!",
        'inactive': "Bu profil faol emas.",
    }
    class Meta:
        model=UserMod


class RegisterForm(UserCreationForm):

    class Meta:
        model=UserMod
        fields = ("username", "email", "password1", "password2")
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Taqiqlangan belgilar: + - $ % #
        forbidden_chars = r'[+\-\$%#!@%^&*]' 
        
        if re.search(forbidden_chars, username):
            raise ValidationError(
                "Foydalanuvchi nomida (+ - $ % # ! @ % ^ & *) belgilarini ishlatish mumkin emas!"
            )
        return username