from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    stock = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title
