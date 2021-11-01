from django.db import models

class categories(models.Model):
    category_title = models.CharField(max_length=200)
    category_description =models.TextField()

    def __str__(self):
        return self.category_title

class product(models.Model):
    product_title = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_category = models.ForeignKey(categories, models.DO_NOTHING)

    def __str__(self):
        return self.product_title