import re
import requests
from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        api_key = settings.EMAIL_VALIDATION_API_KEY
        response = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}")
        
        if response.status_code == 200:
            result = response.json()
            if result['deliverability'] == 'DELIVERABLE':
                return email
            else:
                raise forms.ValidationError('Email is invalid or undeliverable.')
        else:
            raise forms.ValidationError('Failed to validate email. Please try again later.')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = r'^(?:\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$'
        if not re.match(pattern, phone_number):
            raise forms.ValidationError('Invalid UK phone number format.')
        return phone_number