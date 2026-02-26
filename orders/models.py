from django.db import models
from bun_users.models import UserMod
from bun_core.models import Products


# Create your models here.

class OrderItemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(i.product_price() for i in self)
    def total_quantity(self):
        if self:
            return sum(i.quantity for i in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(to=UserMod, on_delete=models.SET_DEFAULT,related_name='order',default=None,verbose_name="Xaridor")
    phone_number = models.CharField(max_length=15, verbose_name="Telefon")
    address = models.CharField(max_length=100, verbose_name="Manzil")
    card_number = models.CharField(max_length=19, verbose_name="Karta raqami")
    card_expiry = models.CharField(max_length=5, verbose_name="Amal qilish muddati")
    is_paid = models.BooleanField(default=False, verbose_name="To'langan")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
 
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
    class Meta:
        db_table='order'
        verbose_name='Zakaz'
        verbose_name_plural='Zakazlar'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitem', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    objects=OrderItemQuerySet().as_manager()

    def product_price(self):
        return round(self.product.change_price()*self.quantity,2)

    class Meta:
        db_table='order_item'
        verbose_name='Sotilgan Zakaz'
        verbose_name_plural='Sotilgan Zakazlar'