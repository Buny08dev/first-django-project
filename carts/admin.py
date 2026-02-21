from django.contrib import admin
from carts.models import CartsModel
# Register your models here.
 
@admin.register(CartsModel)
class CartsAdmin(admin.ModelAdmin):
    list_display=("user",'product')
    list_display_links=("user",'product')
    readonly_fields = ("created_time",)