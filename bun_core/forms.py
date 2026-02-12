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

class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search',
            'aria-label': 'Search',
        
        },)
    )
    def clean_search(self):
        data = self.cleaned_data['search']
        # masalan: qidiruv matnida raqam bo‘lmasligi kerak
        if any(char.isdigit() for char in data):
            raise forms.ValidationError("Qidiruv matnida raqam bo‘lmasligi kerak!")
        return data