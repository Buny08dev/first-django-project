from django.urls import path

from carts.views import CartsView

urlpatterns = [
    path("login/",CartsView.as_view(),name="login"),

]
