from django import forms
from bun_core.models import Products


class AddProduct(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"
        exclude = ("slug",)
        widgets={
            'name':forms.TextInput(attrs={"placeholder":"name"})
        }