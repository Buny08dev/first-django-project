from django.urls import path

from carts.views import CartsView

urlpatterns = [
    path("cart/",CartsView.as_view(),name="cart"),
]
