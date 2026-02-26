from django.contrib import admin
from bun_users.models import UserMod
from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin

# Register your models here.
# admin.site.register(UserMod)

@admin.register(UserMod)
class User(admin.ModelAdmin):
    inlines=[CartTabAdmin,OrderTabularAdmin,]