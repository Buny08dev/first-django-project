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
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search',
            'aria-label': 'Search',
            
        },),
        # error_messages={'min_length':'togri kirit'},
    )
    def clean_search(self):
        data = self.cleaned_data['search']
        
        if not data:
            return data
        if len(data.strip())<=2:
            raise forms.ValidationError("togri kirit")
        
        
        return data