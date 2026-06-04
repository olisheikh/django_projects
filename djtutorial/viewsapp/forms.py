from django import forms 
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_description', 'product_quantity', 'category', 'image']

    