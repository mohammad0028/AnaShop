from django.contrib.auth.models import User
from django.db import models
from ana_products.models import Product
import os


# Create your models here.


class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    order_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount_price = models.IntegerField()
    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class UsedCoupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
