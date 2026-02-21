from django.urls import path

from carts.views import CartsAddView,CartSChangeView

urlpatterns = [
    path("cart/<slug:slug>",CartsAddView.as_view(),name="cart"),
    path('view/',CartSChangeView.as_view(),name='cart_view')
]
