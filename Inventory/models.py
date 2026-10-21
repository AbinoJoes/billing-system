from django.db import models

# Create your models here.

class ProductsItems(models.Model):
    product_name=models.CharField(max_length=200,null=True)
    product_serialno=models.CharField(max_length=200,null=True)
    product_price=models.FloatField(default=0)
    product_gst=models.IntegerField(default=0)


    def __str__(self):
        return self.product_name 

class ContactDetail(models.Model):
    customer_name=models.CharField(max_length=200,null=True)
    email_address=models.EmailField(null=True)

    SUBJECT_CHOICES = [
        ('Customer Management', 'Customer Management'),
        ('Product Management', 'Product Management'),
        ('Order Management', 'Order Management'),
        ('Billing Issue', 'Billing Issue'),
        ('Other', 'Other'),
    ]
    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES
    )
    message=models.TextField(null=True)

    def __str__(self):
        return self.customer_name
