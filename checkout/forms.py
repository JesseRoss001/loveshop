import requests
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import UserProfile

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['postal_code', 'address_line_1', 'address_line_2', 'city', 'country']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels and set autofocus on the first field.
        """
        super(AddressForm, self).__init__(*args, **kwargs)
        placeholders = {
            'postal_code': 'Postal Code',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City',
            'country': 'Country',
        }

        self.fields['postal_code'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mb-2 px-2 py-2 rounded shadow form-border'
            self.fields[field].label = False

    def clean_postal_code(self):
        postal_code = self.cleaned_data.get('postal_code').replace(' ', '').upper()
        if not postal_code:
            raise ValidationError('This field is required.')

        # Verify postcode exists using Postcodes.io API
        response = requests.get(f'https://api.postcodes.io/postcodes/{postal_code}/validate')
        if response.status_code == 200:
            data = response.json()
            if data['result']:
                return postal_code
            else:
                raise ValidationError('Please enter a valid UK postal code that exists.')
        else:
            raise ValidationError('Could not verify postal code. Please try again later.')