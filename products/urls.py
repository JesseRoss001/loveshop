from django.urls import path
from . import views
from .views import add_to_cart, view_cart, product_list
app_name = 'products'

urlpatterns = [
    path('', product_list, name='index'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
]