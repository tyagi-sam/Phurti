from django.db import models

class categories(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField()

    def __str__(self):
        return f"Category {self.title}"

class product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(categories, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"Product {self.title}"
