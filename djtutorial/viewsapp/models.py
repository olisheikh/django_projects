from django.db import models
from django.core.exceptions import ValidationError
from tutorial.models import BaseModel

def validate_image(file):
    file_formats = ('.jpg', '.png',)
    file_size = 500 * 1024
    if ((not file.name.lower().endswith(file_formats)) or file.size > file_size):
        raise ValidationError('Only png or jpg or jpeg images are allowed')
    
class Category(BaseModel):
    product_category = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.product_category
    
    
class Products(BaseModel):
    product_name = models.CharField(max_length=20)
    product_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    product_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, validators=[validate_image])
    
    def __str__(self):
        return self.product_name