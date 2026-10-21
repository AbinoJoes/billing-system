from django.forms import ModelForm
from .models import *

class Customer_Form(ModelForm):

    class Meta:
        model=Customers
        fields='__all__'


class Order_Form(ModelForm):

    class Meta:
        model=Orders
        fields=['customer_reference','product_reference','order_num',
                'order_date','product_quantity']