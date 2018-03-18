from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller_image = models.CharField(max_length=1024)
    seller_name = models.CharField(max_length=1000)
    ratings = models.FloatField(default=0.0)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ['id']


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=1000, default='')
    price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    url = models.CharField(max_length=1024)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id) + ' -- ' + self.product_name

    class Meta:
        ordering = ['product_id']
        verbose_name = "Product"
        verbose_name_plural = "Products"
