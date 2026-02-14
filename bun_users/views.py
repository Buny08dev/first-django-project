from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.views.generic import TemplateView,FormView
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from bun_users.forms import LoginForm,RegisterForm
from django.views.generic.base import View
from django.views import View
from django.urls import reverse_lazy
# from django.contrib.auth.views import LoginView
# Create your views here.

class Registerview(FormView):
    template_name='registrate.html'
    form_class=RegisterForm
    success_url = reverse_lazy('news')

    def form_valid(self, form:RegisterForm):
        
        print("*"*100,form.cleaned_data)

        # user=form.save()
        # login(self.request,user)

        return super().form_valid(form)
    
    def form_invalid(self, form:RegisterForm):

        # print(form.cleaned_data)
        
        return super().form_invalid(form)


class Loginview(FormView):
    form_class=LoginForm
    template_name='login.html'
    def form_valid(self,form:LoginForm):
        if self.request.POST.get('login')=='login':
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
        else:
            return redirect('reg')
    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['form_2']=RegisterForm()
    #     return context