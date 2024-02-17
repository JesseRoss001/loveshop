from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')], blank=True)
    postal_code = models.CharField(max_length=8, validators=[RegexValidator(regex=r'^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$', message='Please enter a valid UK postal code.')], blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username