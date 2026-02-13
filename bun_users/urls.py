from django.urls import path

from bun_users.views import Registerview,Loginview

urlpatterns = [
    path("login/",Loginview.as_view(),name="login"),
    path("profile/",Registerview.as_view(),name="profile"),
    path("registration/",Registerview.as_view(),name="reg"),
    path("logout/",Registerview.as_view(),name="logout"),
]
