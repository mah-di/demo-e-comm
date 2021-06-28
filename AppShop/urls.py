from django.urls import path
from . import views


app_name = 'AppShop'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>/', views.ProductDetails.as_view(), name='product_detail'),
]