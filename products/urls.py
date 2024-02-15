from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='index'),  # Assuming a view named product_list
]