from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
#Employee_adding
@login_required(login_url='/')
def CustomerAdding(request):
        
    context= {
          'customer_detail':Customer_Form()
    }

    if request.method =="POST":
        customer_save=Customer_Form(request.POST)
        if customer_save.is_valid():
            customer_save.save()

    return render(request,'customer_add.html',context)

#view all product
@login_required(login_url='/')
def AllCustomer(request):
    context={
        'all_customer':Customers.objects.all()
    }
    return render(request,'customer_all.html',context)

#deleteRow

def DeleteCustomer(request,id):
    delete_row=Customers.objects.get(id = id)
    delete_row.delete()

    return redirect('/order/customerall/')

#updateRow
def UpdateCustomer(request,id):
    selected_customer=Customers.objects.get(id = id)

    context={
       'customer_detail':Customer_Form(instance=selected_customer)
    }
    if request.method == "POST":
         customer_update=Customer_Form(request.POST,instance=selected_customer)
         if customer_update.is_valid():
             customer_update.save()
             return redirect('/order/customerall/')
    return render(request,'customer_add.html',context)

#orderedForm
@login_required(login_url='/')
def OrderAdd(request):

    context={
        'order_detail':Order_Form()
    }
    if request.method == "POST":

        selected_product=ProductsItems.objects.get(id=request.POST['product_reference'])
        amount=float(selected_product.product_price) * float(request.POST['product_quantity'])
        gst_amount=(amount*selected_product.product_gst)/100
        bill_amount=amount+gst_amount

        new_order=Orders(customer_reference_id=request.POST['customer_reference'],
                         product_reference_id=request.POST['product_reference'],
                         order_num=request.POST['order_num'],order_date=request.POST['order_date'],
                         product_quantity=request.POST['product_quantity'],product_amount=amount,
                         product_gst=gst_amount,bill_amount=bill_amount)

        new_order.save()

    return render(request,'order_add.html',context)

#view all ordered datas
@login_required(login_url='/')
def AllOrders(request):

    context={
        'all_order':Orders.objects.all()
    }

    return render(request,'order_all.html',context)

#deleteRow in orders
def DeleteOrders(request,id):
    delete_row=Orders.objects.get(id = id)
    delete_row.delete()

    return redirect('/order/orderall/')


#updateRow in orders
def UpdateOrders(request,id):
    selected_order=Orders.objects.get(id = id)

    context={
       'order_detail':Order_Form(instance=selected_order)
    }
    if request.method == "POST":
        
        selected_product=ProductsItems.objects.get(id=request.POST['product_reference'])
        amount=float(selected_product.product_price) * float(request.POST['product_quantity'])
        gst_amount=(amount*selected_product.product_gst)/100
        bill_amount=amount+gst_amount

#filter is used to update the products
        order_filter=Orders.objects.filter(id=id)

        order_filter.update(customer_reference_id=request.POST['customer_reference'],
                            product_reference_id=request.POST['product_reference'],
                            order_num=request.POST['order_num'],order_date=request.POST['order_date'],
                            product_quantity=request.POST['product_quantity'],product_amount=amount,
                            product_gst=gst_amount,bill_amount=bill_amount)

         
        return redirect('/order/orderall/')
         
    return render(request,'order_add.html',context)




#billing
@login_required(login_url='/')
def BillingPage(request):
    orders =Orders.objects.select_related(
        'customer_reference',
        'product_reference'
    ).all().order_by('-id')

    billing_data = []
    total_amount = 0
    paid_amount = 0
    pending_amount = 0

    search = request.GET.get('search', '').strip()
    selected_status = request.GET.get('status', '')

    for order in orders:
        total = order.bill_amount or 0

        # Requires a paid_amount field in your Orders model
        paid = getattr(order, 'paid_amount', 0) or 0
        pending = max(total - paid, 0)

        if paid >= total:
            status = 'Paid'
        elif paid > 0:
            status = 'Partial'
        else:
            status = 'Pending'

        customer = order.customer_reference

        customer_name = (
            getattr(customer, 'customer_name', None)
            or getattr(customer, 'name', None)
            or str(customer)
        )

        invoice_number = getattr(order, 'order_num', None) or order.pk

        record = {
            'id': order.pk,
            'invoice_number': invoice_number,
            'customer_name': customer_name,
            'order_date': getattr(order, 'order_date', None),
            'quantity': getattr(order, 'product_quantity', 0),
            'product_amount': getattr(order, 'product_amount', 0) or 0,
            'gst': getattr(order, 'product_gst', 0) or 0,
            'total': total,
            'paid': paid,
            'pending': pending,
            'status': status,
        }

        

        if search:
            searchable = (
                str(invoice_number) + ' ' + customer_name
            ).lower()

            if search.lower() not in searchable:
                continue

        if selected_status and status != selected_status:
            continue

        billing_data.append(record)

        total_amount += total
        paid_amount += paid
        pending_amount += pending

    context = {
        'billing_records': billing_data,
        'total_invoices': len(billing_data),
        'total_amount': total_amount,
        'paid_amount': paid_amount,
        'pending_amount': pending_amount,
        'selected_status': selected_status,
        'search': search,
    }

    return render(request, 'billing.html', context)


def billsearch(request):
    search = request.GET.get('search', '').strip()

    if search:
        billing_records = [
            record for record in billing_records
            if search.lower() in str(record.get('customer_name', '')).lower()
            or search.lower() in str(record.get('customer_id', '')).lower()
        ]
    return render(request,'billing.html')