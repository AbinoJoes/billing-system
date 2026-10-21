from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


#HomePage
class HomePage(LoginRequiredMixin, View):

    login_url = '/'

    def get(self,request):
        return render(request,'home.html')





#ContactPage
# def ContactPage(request):
   
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         ContactDetail.objects.create(
#             customer_name=name,
#             email_address=email,
#             subject=subject,
#             message=message
#         )

#         return redirect('') 

#     return render(request, 'contact.html')

#Product_adding
# def ProductAdding(request):
        
#     context= {
#           'Product_detail':Product_Form()
#     }

#     if request.method =="POST":
#         product_save=Product_Form(request.POST)
#         if product_save.is_valid():
#             product_save.save()

#     return render(request,'products_add.html',context)


#view all product
# def AllProduct(request):
#     context={
#         'all_product':ProductsItems.objects.all()
#     }
#     return render(request,'product_all.html',context)

#deleteRow
# def DeleteProduct(request,id):
#     delete_row=ProductsItems.objects.get(id = id)
#     delete_row.delete()

#     return redirect('/Inventory/productall/')

#updateRow
# def UpdateProducts(request,id):
#     selected_product=ProductsItems.objects.get(id = id)

#     context={
#        'Product_detail':Product_Form(instance=selected_product)
#     }
#     if request.method == "POST":
#          product_update=Product_Form(request.POST,instance=selected_product)
#          if product_update.is_valid():
#              product_update.save()
#              return redirect('/Inventory/productall/')
#     return render(request,'products_add.html',context)



#conatact adding
class ContactPage(LoginRequiredMixin, View):

    login_url='/'

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactDetail.objects.create(
            customer_name=name,
            email_address=email,
            subject=subject,
            message=message
        )

        return redirect('/Inventory/contact/')

#Product_adding
class ProductAdding(LoginRequiredMixin, View):

    login_url='/'

    def get(self,request):
        context= {
           'Product_detail':Product_Form()
               }
        return render(request,'products_add.html',context)

    def post(self,request):

        product_save=Product_Form(request.POST)
        if product_save.is_valid():
           product_save.save()

        return redirect('/Inventory/product/')


#view all product
class AllProduct(View):
    def get(self,request):
            context={
                'all_product':ProductsItems.objects.all()
            }
            return render(request,'product_all.html',context)

#deleteRow
class DeleteProduct(View):
    def get(self,request,id):
        def DeleteProduct(request,id):
         delete_row=ProductsItems.objects.get(id = id)
         delete_row.delete()

         return redirect('/Inventory/productall/')

#updateRow
class UpdateProducts(View):
    def get(self,request,id):
        selected_product=ProductsItems.objects.get(id = id)
        
        context={
               'Product_detail':Product_Form(instance=selected_product)
            }
        return render(request,'products_add.html',context)

    def post(self,request,id):
        selected_product=ProductsItems.objects.get(id = id)
        product_update=Product_Form(request.POST,instance=selected_product)
        if product_update.is_valid():
            product_update.save()
            return redirect('/Inventory/productall/')
