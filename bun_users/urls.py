from django.urls import path

from bun_users.views import Registerview,Loginview,LogoutView,ProfileView

urlpatterns = [
    path("login/",Loginview.as_view(),name="login"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("registration/",Registerview.as_view(),name="reg"),
    path("logout/",LogoutView.as_view(),name="logout"),
]
