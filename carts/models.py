from django.db import models
from bun_users.models import UserMod
from bun_core.models import Products



class CartQueryset(models.QuerySet):
    def totel_price(self):
        print(self)
        return sum(cart.purchase()  for cart in self)
    def total_quantity(self):
        ...

# Create your models here.
class CartsModel(models.Model):
    user=models.ForeignKey(to=UserMod,on_delete=models.CASCADE,related_name="carts",verbose_name='carts')
    product=models.ForeignKey(to=Products,on_delete=models.CASCADE,related_name="products",verbose_name='products')
    quantity=models.PositiveSmallIntegerField(default=0,verbose_name="soni")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="qoshilgan vaqti")
    
    objects=CartQueryset.as_manager()

    class Meta:
        verbose_name="savatcha"
        verbose_name_plural="savatchalar"

    def __str__(self):
        return f"Savatcha:{self.user.username},Product:{self.product.name},Soni:{self.quantity}"
    
    def purchase(self):
        return round(self.product.change_price()*self.quantity,2)
