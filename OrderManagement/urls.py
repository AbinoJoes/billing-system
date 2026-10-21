from django.urls import path
from .views import *

urlpatterns=[
   path('customer/',CustomerAdding),
   path('customerall/',AllCustomer),
   path('customerdelete/<int:id>/',DeleteCustomer, name='delete_items'),
   path('customerupdate/<int:id>/',UpdateCustomer, name='update_items'),
   path('orderadd/',OrderAdd),
   path('orderall/',AllOrders),
   path('orderdelete/<int:id>/',DeleteOrders, name='delete_order_items'),
   path('orderupdate/<int:id>/',UpdateOrders, name='update_order_items'),
   path('billingpage/',BillingPage),
   path('billsearch/', billsearch)
]