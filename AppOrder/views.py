from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required


# Models
from .models import Cart, Order
from AppShop.models import Product


# Messages
from django.contrib import messages


@login_required
def add_to_cart(req, pk):
    item = get_object_or_404(Product,pk=pk)
    cart = Cart.objects.get_or_create(user=req.user, item=item, purchased=False)[0]
    order_qset = Order.objects.filter(user=req.user, ordered=False)

    if order_qset.exists():
        order = order_qset[0]

        if order.carts.filter(item=item):
            cart.quantity += 1
            cart.save()
        else:
            order.carts.add(cart)
            order.save()
        
        messages.success(req, "Cart updated.")
    else:
        order = Order.objects.create(user=req.user)
        order.carts.add(cart)
        order.save()
        messages.success(req, "Item added to cart.")

    return redirect('AppShop:home')


@login_required
def cart(req):
    order = Order.objects.filter(user = req.user, ordered=False).first()
    carts = Cart.objects.filter(user=req.user, purchased=False)

    return render(req, 'AppOrder/cart.html', context={'order':order, 'carts':carts})


@login_required
def increase(req, pk):
    cart = Cart.objects.get(pk=pk)
    cart.quantity += 1
    cart.save()
    messages.info(req, "Cart item quantity updated.")
    
    return redirect(req.META['HTTP_REFERER'])


@login_required
def decrease(req, pk):
    cart = Cart.objects.get(pk=pk)
    cart.quantity -= 1
    cart.save()
    messages.info(req, "Cart item quantity updated.")
    
    return redirect(req.META['HTTP_REFERER'])


@login_required
def remove(req, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    order = Order.objects.get(user=req.user, ordered=False)
    messages.warning(req, "Item removed from cart.")

    if order.carts.count() == 0:
        order.delete()
    
    return redirect(req.META['HTTP_REFERER'])



@login_required
def customer_orders(req):
    try:
        orders = Order.objects.filter(user=req.user, ordered=True)
        context = {'orders':orders}
    except:
        messages.info(req, 'You Do Not Have Any Orders.')
        return redirect('AppShop:home')
    
    return render(req, 'AppOrder/orders.html', context=context)