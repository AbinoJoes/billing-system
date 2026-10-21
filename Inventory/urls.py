from django.urls import path
from .views import *

urlpatterns=[
    path('home/',HomePage.as_view()),
    path('contact/',ContactPage.as_view()),
    path('product/',ProductAdding.as_view()),
    path('productall/',AllProduct.as_view()),
    path('productdelete/<int:id>/',DeleteProduct.as_view(), name='delete_product_items'),
    path('productupdate/<int:id>/',UpdateProducts.as_view(), name='update_product_items')
]