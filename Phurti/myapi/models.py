from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField()

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Categories, default=1, on_delete=models.SET_DEFAULT)
