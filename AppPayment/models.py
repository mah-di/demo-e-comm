from django.db import models

# Models
from django.conf import settings

# Create your models here.



class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='billing_address')
    address = models.CharField(max_length=200, verbose_name='Full Shipping Address', null=True)
    city = models.CharField(max_length=40, verbose_name='City', null=True)
    country = models.CharField(max_length=40, verbose_name='Country', null=True)
    zipcode = models.CharField(max_length=10, verbose_name='Area Post Code', null=True)
    phone = models.CharField(max_length=15, verbose_name='Contact Number', null=True)


    def __str__(self):
        return self.user.email


    def is_fully_setup(self):
        fields = [f.name for f in self._meta.get_fields()]
        
        for field in fields:
            value = getattr(self, field)
            
            if value is None or value == '':
                return False
        
        return True