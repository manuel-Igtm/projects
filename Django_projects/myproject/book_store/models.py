from django.db import models

# Create your models here. 
# Create a Django model called Product with fields like name, description, price, and category

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    category = models.ForeignKey(Category,on_delete = models.CASCADE, related_name = "products", default = 0)
