from django.db import models
from bun_users.models import UserMod
from bun_core.models import Products



class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.purchase() for cart in self)
    
    def total_quantity(self):
        # print(self)
        if self:
            return sum(i.quantity for i in self)
        return 0

# Create your models here.
class CartsModel(models.Model):
    user=models.ForeignKey(to=UserMod,on_delete=models.CASCADE,blank=True,null=True,related_name="carts",verbose_name='User')
    product=models.ForeignKey(to=Products,on_delete=models.CASCADE,related_name="products",verbose_name='Product')
    quantity=models.PositiveSmallIntegerField(default=0,verbose_name="Soni")
    session_key=models.CharField(max_length=32,null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="Qoshilgan vaqti")
    
    objects=CartQueryset.as_manager()

    class Meta:
        db_table="savat"
        verbose_name="savatcha"
        verbose_name_plural="savatchalar"

    def __str__(self):
        return f"Savatcha:{self.user.username if self.user else "Anonimus"} | Product:{self.product.name} | Soni:{self.quantity}"
    
    def purchase(self):
        return round(self.product.change_price()*self.quantity,2)
