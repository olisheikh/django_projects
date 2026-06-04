from django.db import models
from tutorial.models import BaseModel
# Create your models here.
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
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    def __str__(self):
        return self.product_name