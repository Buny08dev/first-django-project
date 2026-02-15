from django.shortcuts import redirect
# registratsiya bolimi bilan ishlash
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
# form va kerakli importlar
from bun_users.forms import LoginForm,RegisterForm
from django.views.generic import TemplateView,FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
# from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# keshlar bilan ishlash
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# pip install django-phonenumber-field


# Create your views here.
class AnonymousRequiredMixin:
    @method_decorator(never_cache) # Keshni o'chirish
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # bu yerda not page orniga maxsus joy
            return redirect('news')
        return super().dispatch(request, *args, **kwargs)


class Registerview(AnonymousRequiredMixin,FormView):
    template_name='registrate.html'
    form_class=RegisterForm
    success_url = reverse_lazy('news')

    def form_valid(self, form:RegisterForm):
        # print("*"*100,form.cleaned_data,)
        user=form.save()
        login(self.request,user)
        messages.success(self.request,f'Xush kelibsiz {user.username}')
        return super().form_valid(form)


class Loginview(AnonymousRequiredMixin,FormView):
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
                messages.success(self.request,f'Xush kelibsiz {username}')
                return redirect('news')
            else:
                form.add_error(None, "Ism yoki parol xato kiritildi!")
                return self.form_invalid(form)
        else:
            return redirect('reg')

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        messages.error(request, f"{request.user.username}dan chiqib ketdinggiz")
        logout(request)
        return redirect('news')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"