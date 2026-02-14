from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.views.generic import TemplateView,FormView
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from bun_users.forms import UsersForm,RegisterForm
# from django.contrib.auth.views import LoginView
# Create your views here.

class Registerview(FormView):
    template_name='login.html'
    form_class=RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_signup'] = True   # 🔥 MUHIM
        return context

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['show_signup'] = True
        return self.render_to_response(context)

class Loginview(FormView):
    form_class=UsersForm
    template_name='login.html'
    
    def form_valid(self,form:UsersForm):
        # print(self.request.POST)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        user=authenticate(username=username, password=password)
    
        # print(user,'*'*100)
    
        if user is not None:
            login(self.request,user)
            return redirect('news')
        else:
            form.add_error(None, "Ism yoki parol xato kiritildi!")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        # print(self.request.POST)
        # print("Xatoliklar lug'ati:", form.non_field_errors)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_signup'] = False
        return context