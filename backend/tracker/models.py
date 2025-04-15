from django.db import models
from django.contrib.auth import get_user_model
from .constants import ProductStatus , Markets


User = get_user_model()

    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/')
    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=ProductStatus.choices, default=ProductStatus.DOING)
    market = models.IntegerField(choices=Markets.choices, default=Markets.UZUM_MARKET)
    url = models.URLField()
    now_price = models.DecimalField(max_digits=10, decimal_places=2)
    error_message = models.TextField(blank=True, null=True)
    target = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.price} on {self.date}"
    
