from django.contrib import admin
from orders.models import Order,OrderItem
# Register your models here.

class OrderItemTabularAdmin(admin.TabularInline):
    model=OrderItem
    fields=('order','product','price','quantity',)
    extra=0
class OrderTabularAdmin(admin.TabularInline):
    model=Order
    fields=('address','card_number','card_expiry','is_paid')
    extra=0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=(OrderItemTabularAdmin,)

@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields=('created_time',)
    
