from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class fooditems(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    decription = models.TextField()
    photo = models.ImageField(upload_to='foodimages/')

    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    item = models.ForeignKey(fooditems, related_name='orders', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

    
class cartitems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(fooditems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"