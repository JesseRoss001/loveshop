from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
            user_profile.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

     
        # Sets placeholder on inputs
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password 1'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password 2'

        self.fields['username'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Adds stylings classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'mb-3 px-2 py-2 rounded shadow text-black form-border')
            self.fields[field].label = False