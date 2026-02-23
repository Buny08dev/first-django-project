from django.contrib import admin
from carts.models import CartsModel
# Register your models here.
 

class CartTabAdmin(admin.TabularInline):
    model=CartsModel
    fields=('product','quantity','created_time')
    readonly_fields=('created_time',)
    extra=1

@admin.register(CartsModel)
class CartsAdmin(admin.ModelAdmin):
    list_display=("user",'product')
    list_display_links=("user",'product')
    readonly_fields = ("created_time",)