from django.contrib import admin
from bun_core.models import bunbase,Categories,Products



# Register your models here.


# admin.site.register(bunbase)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name")
    list_display_links = ("name",)
    prepopulated_fields={"slug":('name',)} 
    

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name","price",'created_time')
    list_display_links = ("name",)
    list_editable = ("price",)
    prepopulated_fields={"slug":('name',)}
    list_filter = ("created_time", "price")
    search_fields = ("name", "slug")
    list_per_page = 8
    # date_hierarchy = "created_time"
