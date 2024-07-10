from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    Cusfirst_name = models.CharField(max_length=100)
    Cuslast_name = models.CharField(max_length=100)
    Cusemail = models.CharField(max_length=100)
    Cusphone = models.CharField(max_length=20)

class Product(models.Model):
    productId = models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    productQuantity = models.CharField(max_length=10)

class ExistUser(models.Model):
    Ex_email = models.CharField(max_length=100)
    Ex_password = models.CharField(max_length=100)

class RegisterUser(models.Model):
    Reg_first_name = models.CharField(max_length=100)
    Reg_last_name = models.CharField(max_length=100)
    Reg_email = models.CharField(max_length=100)
    Reg_password = models.CharField(max_length=100)

# Market/models.py


class Member(models.Model):
    name = models.CharField(max_length=100)
    is_latest = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('processing', 'Processing'), ('delivered', 'Delivered'), ('shipped', 'Shipped')])
    product = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} - {self.product}'

class Stock(models.Model):
    item = models.CharField(max_length=100)
    in_stock = models.IntegerField()
    out_stock = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.item
