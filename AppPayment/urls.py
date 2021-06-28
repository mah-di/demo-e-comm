from django.urls import path
from . import views


app_name = 'AppPayment'


urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('gateway/', views.payment, name='payment'),
    path('order-status/', views.payment_status, name='status'),
    path('confirmation/<validation_id>/<transaction_id>/', views.confirmation, name='confirmation'),
]