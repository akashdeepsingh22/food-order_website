from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    
    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='orders', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} (Order {self.order.id})"


# Create your models here.
class fooditems(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    decription = models.TextField()
    photo = models.ImageField(upload_to='foodimages/')

    def __str__(self):
        return self.name
