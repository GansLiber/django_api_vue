from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=timezone.now)
    is_exist = models.BooleanField(default=False)
    email = models.EmailField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)

