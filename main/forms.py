from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "price", "stock", "description", "category", "thumbnail", "is_featured"]
    
    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        return strip_tags(product_name)
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)