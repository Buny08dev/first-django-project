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
            # 'required': False ,
        }),
        error_messages={"required":"Majburiy bolim"}
    )
    password = forms.CharField(
        label="Parol", # 'Password' o'rniga 'Parol' chiqadi
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'auth-form-group',
            'placeholder': 'Parol',
            # 'required': False ,
        }),
        error_messages={"required":"Majburiy bolim"}
    )
    error_messages = {
        'invalid_login': "Ism yoki parol xato kiritildi. Iltimos, qaytadan tekshiring!",
        'inactive': "Bu profil faol emas.",
    }
    class Meta:
        model=UserMod


class RegisterForm(UserCreationForm):

    # password1=forms.CharField(required=True,widget=forms.TextInput(attrs={"":""}),error_messages={"required":"idinaxuy"})
    
    class Meta:
        model=UserMod
        fields = ("username", "email", "phone", "password1", "password2")
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Taqiqlangan belgilar: + - $ % #
        forbidden_chars = r'[+\-\$%#!@%^&*]' 
        
        if re.search(forbidden_chars, username):
            raise ValidationError(
                "Foydalanuvchi nomida (+ - $ % # ! @ % ^ & *) belgilarini ishlatish mumkin emas!"
            )
        
        return username
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not re.match(r'^\+998\d{9}$', phone):
            raise ValidationError("Telefon raqam +998(XX)-XXX-XX-XX formatda bo‘lishi kerak")
        if UserMod.objects.filter(phone=phone).exists():
            raise ValidationError("Bu telefon raqam allaqachon mavjud!")
        return phone