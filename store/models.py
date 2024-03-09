from django.contrib.auth.hashers import make_password
from django.db import models
import datetime


# Products Category Model
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


# Products Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/productsImg")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Securely hash and store password
    def set_password(self, raw_password):
        self.password = make_password(raw_password)


# Customer Order Model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
