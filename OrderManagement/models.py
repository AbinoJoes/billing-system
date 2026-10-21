from django.db import models
from Inventory.models import ProductsItems

# Create your models here.
class Customers(models.Model):
    customer_id=models.CharField(max_length=200,null=True)
    customer_since=models.CharField(max_length=200,null=True)
  


    def __str__(self):
        return self.customer_id 


#add foreign key

class Orders(models.Model):
    customer_reference=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True)
    product_reference=models.ForeignKey(ProductsItems,on_delete=models.SET_NULL,null=True)
    order_num=models.CharField(max_length=50,null=True)
    order_date=models.CharField(max_length=50,null=True)
    product_quantity=models.FloatField(default=0)
    product_amount=models.FloatField(default=0)
    product_gst=models.IntegerField(default=0)
    bill_amount=models.FloatField(default=0)

    def __str__(self):
        return self.order_num
    

class filter(models.Model):
    search=models.CharField(max_length=100)