from django.urls import path

from carts.views import CartsAddView,CartSChangeView,CartRemoveView

urlpatterns = [
    path("cart/<slug:slug>",CartsAddView.as_view(),name="cart"),
    path('cart_view/',CartSChangeView.as_view(),name='cart_view'),
    path('cart_remove_view/<int:pk>/',CartRemoveView.as_view(),name='cart_remove')
]
