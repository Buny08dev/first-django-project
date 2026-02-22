from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,ListView,DeleteView
from bun_core.models import Products
from carts.models import CartsModel
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
# Create your views here.

class CartsAddView(View):
    def post(self,request,slug):
        # print(request.GET,slug)
        product=Products.objects.get(slug=slug)
        # print(product)
        if request.user.is_authenticated:
            carts=CartsModel.objects.filter(user=request.user,product=product)
            if carts.exists():
                # print(carts)
                cart= carts.first()
                # print(cart)
                if cart:
                    cart.quantity+=1
                    cart.save() 
            else:
                CartsModel.objects.create(user=request.user,product=product,quantity=1)
        # return redirect(request.META['HTTP_REFERER'])
        return redirect('cart_view')

class CartSChangeView(ListView):
    template_name = 'carts.html'
    model = CartsModel
    context_object_name = 'carts'

    def get_queryset(self):
        return CartsModel.objects.filter(user=self.request.user)

class CartQuantityChangeView(View):
    def post(self, request, pk):
        cart = get_object_or_404(CartsModel, pk=pk)
        product = cart.product
        action = request.POST.get("action")

        if action == "plus":
            if cart.quantity < product.quantity:
                cart.quantity += 1
                cart.save()
            else:
                return JsonResponse({
                        "success": False,
                        "error": "max",
                        "message": "Omborda bundan ko‘p mahsulot yo‘q",
                        "quantity": cart.quantity,
                        "total_price": cart.purchase(),
                        "max": product.quantity
                    })

        elif action == "minus":
            if cart.quantity > 1:
                cart.quantity -= 1
                cart.save()
            else:
                cart.delete()
                return JsonResponse({"deleted": True})

        return JsonResponse({
                "success": True,
                "quantity": cart.quantity,
                "total_price": cart.purchase(),
                "max": product.quantity
            })

class CartRemoveView(DeleteView):
    template_name='carts.html'
    model=CartsModel
    context_object_name='carts'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')