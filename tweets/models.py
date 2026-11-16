from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    content = models.CharField(max_length=200)
    description = models.TextField(default='')
    likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.content[:30]


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateTimeField(default=None, null=True, blank=True)
    offer = models.BooleanField(default=False,blank=True)
    sku = models.CharField(default=0, max_length=50, unique=True)
    
    delivery_status = [
        ("p", "pending"),
        ("s", "shipped"),
        ("d", "delivered")
    ]
    
    delivery = models.CharField(max_length=1, choices=delivery_status, default="p")
    