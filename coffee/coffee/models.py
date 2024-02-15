from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    PRODUCT_CAT = [(1, "COFFEE"), (2, "CAPSULE"), (3, "CUPS"), (4, "ACC")]
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)
    src = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.SmallIntegerField(choices=PRODUCT_CAT, default=1)
    jjim = models.ManyToManyField(User, related_name="jjim")
