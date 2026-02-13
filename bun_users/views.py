from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.views.generic import TemplateView,FormView
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from bun_users.forms import UsersForm
# from django.contrib.auth.views import LoginView
# Create your views here.

class Registerview(TemplateView):
    template_name='login.html'

   

class Loginview(FormView):
    form_class=UsersForm
    template_name='login.html'
    
    def form_valid(self,form:UsersForm):

        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        user=authenticate(username=username, password=password)
    
        print(user,'*'*100)
    
        if user is not None:
            login(self.request,user)
            return redirect('news')
        else:
            form.add_error(None, "Ism yoki parol xato kiritildi!")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        print("Xatoliklar lug'ati:", form.non_field_errors)
        return super().form_invalid(form)