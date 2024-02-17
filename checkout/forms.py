# checkout/forms.py
from django import forms
from accounts.models import UserProfile

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['postal_code', 'address_line_1', 'address_line_2', 'city', 'country']
