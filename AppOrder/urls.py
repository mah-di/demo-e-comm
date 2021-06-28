from django.urls import path
from . import views


app_name = 'AppOrder'


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-to-cart/<pk>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<pk>/', views.increase, name='increase'),
    path('decrease/<pk>/', views.decrease, name='decrease'),
    path('remove-from-cart/<pk>/', views.remove, name='remove'),
    path('my-orders/', views.customer_orders, name='orders'),
]