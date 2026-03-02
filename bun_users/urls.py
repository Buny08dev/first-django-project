from django.urls import path

from bun_users.views import Registerview,Loginview,LogoutView,ProfileView,VerifyEmailView,ResendCodeView

urlpatterns = [
    path("login/",Loginview.as_view(),name="login"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("registration/",Registerview.as_view(),name="reg"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("verify/",VerifyEmailView.as_view(),name="verify"),
    path("verifycorrect/",ResendCodeView.as_view(),name="verifycor"),
]
