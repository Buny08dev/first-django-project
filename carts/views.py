from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from bun_core.models import Products
from carts.models import CartsModel

# Create your views here.

class CartsAddView(View):
    def get(self,request,slug):
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
    template_name='carts.html'
    model=CartsModel
    context_object_name='carts'

    # def get(self,request):
    #     return render(request,'carts.html')