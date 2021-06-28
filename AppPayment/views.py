from django.shortcuts import redirect, render
from django.urls import reverse

# Models & Forms
from .models import BillingAddress
from AppOrder.models import Cart, Order
from .forms import BillingForm, ProfileCheckForm

# Authentication
from django.contrib.auth.decorators import login_required

# Messages
from django.contrib import messages

# Payment
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt



@login_required
def checkout(req):
    address = BillingAddress.objects.get_or_create(user=req.user)
    address = address[0]
    form = BillingForm(instance=address)
    form2 = ProfileCheckForm(instance=req.user.profile)

    if req.method == 'POST':
        form = BillingForm(data=req.POST, instance=address)
        form2 = ProfileCheckForm(data=req.POST, instance=req.user.profile)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(req, "Shipping address and information saved!")

    order = Order.objects.get(user=req.user, ordered=False)
    return render(req, 'AppPayment/checkout.html', context={'form':form, 'form2':form2, 'order':order, 'address':address})



@login_required
def payment(req):
    shipping_address = BillingAddress.objects.get_or_create(user=req.user)[0]

    if not shipping_address.is_fully_setup() or not req.user.profile.is_fully_setup():
        messages.warning(req, 'Please provide all the necessary informations.')
        return redirect('AppPayment:checkout')
    

    store_id = 'abd60d890adf2b3e'
    API_Key = 'abd60d890adf2b3e@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_Key)


    status_url = req.build_absolute_uri(reverse('AppPayment:status'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)


    order = Order.objects.get(user=req.user, ordered=False)
    items = order.carts.all()
    item_count = 0
    for item in items:
        item_count += item.quantity
        
    mypayment.set_product_integration(total_amount=Decimal(order.get_total()), currency='BDT', product_category='Mixed', product_name=items, num_of_item=item_count, shipping_method='Courier', product_profile='None')


    mypayment.set_customer_info(name=req.user.profile.full_name, email=req.user.email, address1=req.user.profile.address_1, address2='', city=req.user.profile.city, postcode=req.user.profile.zip_code, country=req.user.profile.country, phone=req.user.profile.phone)


    mypayment.set_shipping_info(shipping_to=req.user.profile.full_name, address=shipping_address.address, city=shipping_address.city, postcode=shipping_address.zipcode, country=shipping_address.country)


    response = mypayment.init_payment()


    return redirect(response['GatewayPageURL'])



@csrf_exempt
def payment_status(req):
    if req.method == 'POST' or req.method == 'post':
        payment_data = req.POST

    status = payment_data['status']
    
    if status == 'VALID':
        transaction_id = payment_data['tran_id']
        validation_id = payment_data['val_id']
        return redirect('AppPayment:confirmation', validation_id, transaction_id)
    
    else:
        messages.warning(req, "An Unexpected Error Occured, Couldn't Complete The Payment Process. Please Try Again.")

        return redirect('AppPayment:checkout')



@login_required
def confirmation(req, validation_id, transaction_id):
    order = Order.objects.get(user=req.user, ordered=False)
    carts = Cart.objects.filter(user=req.user, purchased=False)

    order.order_id = validation_id
    order.transaction_id = transaction_id
    order.ordered = True
    order.save()

    for cart in carts:
        cart.purchased = True
        cart.save()
    
    messages.success(req, 'Payment Successfull!')
    return render(req, 'AppPayment/status.html', context={})