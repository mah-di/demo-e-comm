from django.db import models
from AppLogin.models import User
from AppShop.models import Product

# Create your models here.



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='carts')
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'


    def get_total(self):
        return format(float(self.item.discounted_price*self.quantity), '.2f')



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    carts = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now=True)


    def get_total(self):
        total = 0

        for item in self.carts.all():
            total += float(item.get_total())

        return total