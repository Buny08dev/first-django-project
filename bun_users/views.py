from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.views.generic import TemplateView
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User

# Create your views here.

class Registerview(TemplateView):
    template_name='login.html'

    def post(self,*args,**kwargs):
        username=self.request.POST.get('username')
        password=self.request.POST.get('password')
        email=self.request.POST.get('email',None)
        login_pass=self.request.POST.get('login')
        
        user=authenticate(self.request, username=username, password=password)

        if login_pass=="login":
            login(self.request,user)
            return redirect('news')
        elif login_pass=='sign on':
            user = User.objects.create(username=username,email=email,password=password) 
            login(self.request,user)
            return redirect('news')

        return render(self.request,self.template_name)
