from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')], max_length=17, blank=True)  # Adjust the regex as needed for your use case

    def __str__(self):
        return self.user.username