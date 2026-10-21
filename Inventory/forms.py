from django.forms import ModelForm
from .models import *

class Product_Form(ModelForm):

    class Meta:
        model=ProductsItems
        fields='__all__'

class Contact_Form(ModelForm):

    class Meta:
        model=ContactDetail
        fields='__all__'