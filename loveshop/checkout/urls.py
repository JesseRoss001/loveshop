from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout_page, name='index'),  # Assuming a view named checkout_page
]