from django.urls import path

from carts.views import CartsAddView,CartView,CartRemoveView,CartQuantityChangeView

urlpatterns = [
    path("cart/<slug:slug>",CartsAddView.as_view(),name="cart"),
    path('cart_view/',CartView.as_view(),name='cart_view'),
    path('cart_view/<int:pk>/',CartQuantityChangeView.as_view(),name='cart_change'),
    path('cart_remove_view/<int:pk>/',CartRemoveView.as_view(),name='cart_remove')
]
