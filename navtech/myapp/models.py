from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=256)
    product_price = models.CharField(max_length=125)



    def __str__(self) -> str:
        return self.product_name

class Order_Info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    
