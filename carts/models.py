from django.db import models
from bun_users.models import UserMod
from bun_core.models import Products

# Create your models here.
class CartsModel(models.Model):
    user=models.ForeignKey(to=UserMod,on_delete=models.CASCADE,related_name="carts",verbose_name='carts')
    product=models.ForeignKey(to=Products,on_delete=models.CASCADE,related_name="products",verbose_name='products')
    quantity=models.PositiveSmallIntegerField(default=0,verbose_name="soni")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="qoshilgan vaqti")

    class Meta:
        verbose_name="savatcha"
        verbose_name_plural="savatchalar"

    def __str__(self):
        return f"Savatcha:{self.user.username},Product:{self.product.name},Soni:{self.quantity}"