from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from bun_users.models import UserMod
from django import forms

class UsersForm(AuthenticationForm):
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
        meta=UserMod