from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,ListView,DeleteView
from bun_core.models import Products
from carts.models import CartsModel
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.db.models import F
# Create your views here.

class CartsAddView(View):
    def post(self,request,slug):
        # print(request.POST)
        quantity=int(request.POST.get('quantity')[0])
        product=Products.objects.get(slug=slug)
        if request.user.is_authenticated:
            carts=CartsModel.objects.filter(user=request.user,product=product)
            if carts.exists():
                cart= carts.first()
                if cart:
                    cart.quantity=quantity
                    cart.save() 
            else:
                CartsModel.objects.create(user=request.user,product=product,quantity=quantity)
        else:
            if not request.session.session_key:
                request.session.create()
            carts=CartsModel.objects.filter(session_key=request.session.session_key,product=product)
            if carts.exists():
                cart= carts.first()
                if cart:
                    cart.quantity=quantity
                    cart.save() 
            else:
                CartsModel.objects.create(session_key=request.session.session_key,product=product,quantity=quantity)
        # return redirect(request.META['HTTP_REFERER'])
        return redirect('cart_view')

class CartView(ListView):
    template_name = 'carts.html'
    model = CartsModel
    context_object_name = 'carts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return CartsModel.objects.filter(user=self.request.user)
        else:
            if self.request.session.session_key:
                return CartsModel.objects.filter(session_key=self.request.session.session_key)
            else:
                return CartsModel.objects.none()

class CartQuantityChangeView(View):
    def post(self, request, pk):
        cart = get_object_or_404(CartsModel, pk=pk)
        product = cart.product
        action = request.POST.get("action")

        if action == "plus":
            if cart.quantity < product.quantity:
                cart.quantity =F('quantity') + 1
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
                cart.quantity =F('quantity') - 1
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