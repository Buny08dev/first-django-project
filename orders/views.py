from django.shortcuts import render,redirect
from carts.models import CartsModel
from orders.models import Order,OrderItem
from django.views import View
from django.db import transaction
from django.core.exceptions import ValidationError
from django.db.models import F
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class OrderView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.user)
        return render(request,'order.html',{'user':request.user})
    def post(self, request):
        try:
            with transaction.atomic():
                user=request.user
                cart_items=CartsModel.objects.filter(user=user)
               
                print(request.POST.get('card_expiry'))

                if cart_items.exists():
                    order=Order.objects.create(
                        user=user,
                        phone_number=request.user.phone,
                        address=request.POST.get('address'),
                        card_number=request.POST.get('card_number'),
                        card_expiry=request.POST.get('card_expiry'),
                        is_paid=True
                    )
                for cart in cart_items:
                    product=cart.product
                    price=cart.product.change_price()
                    quantity=cart.quantity
                   
                    if product.quantity < quantity:
                        raise ValidationError("skladda yetarlicha mahsulopt yo`q!")
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        price=price,
                        quantity=quantity
                    )
                    product.quantity=F('quantity')-quantity
                    product.save()
                cart_items.delete()
                messages.success(request,"Zakaz qabul qilindi")
                return redirect('profile')
        except ValidationError as error:
            messages.error(request, str(error))
            return redirect('order')