from django import forms

# Models
from .models import BillingAddress
from AppLogin.models import Profile



class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ('address', 'city', 'country', 'zipcode', 'phone',)



class ProfileCheckForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'address_1', 'phone')