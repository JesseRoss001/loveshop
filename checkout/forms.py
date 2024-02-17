# checkout/forms.py
from django import forms
from accounts.models import UserProfile

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['postal_code', 'address_line_1', 'address_line_2', 'city', 'country']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'postal_code': 'Postal Code',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 1',
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

            