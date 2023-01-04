from datetime import datetime
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    

class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published= models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.name)
    