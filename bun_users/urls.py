from django.contrib import admin
from django.urls import path,include

from bun_users.views import Registerview

urlpatterns = [
    path("",Registerview.as_view(),name="login"),]
