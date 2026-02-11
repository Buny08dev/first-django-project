from rest_framework import serializers

from bun_core.models import Products

class ProductsApiForm(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"