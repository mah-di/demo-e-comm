from django.shortcuts import render, get_object_or_404


# Models
from .models import Category, Product


# Class based views
from django.views.generic import ListView, DetailView



class Home(ListView):
    model = Product
    template_name = 'AppShop/home.html'
    context_object_name = 'products'



class ProductDetails(DetailView):
    model = Product
    template_name = 'AppShop/product_detail.html'
    context_object_name = 'product'



def categories(req, category):
    cat = get_object_or_404(Category, title=category)
    products = Product.objects.filter(category=cat)

    return render(req, 'AppShop/home.html', context={'products':products})