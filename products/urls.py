from django.urls import path, include
from . import views
from .views import add_to_cart, view_cart, product_list
from .views import load_view_cart
app_name = 'products'

urlpatterns = [
    path('', product_list, name='index'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/items/', views.cart_items, name='cart_items'),
    path('cart/remove-from-cart/',
         views.remove_from_cart, name='remove_from_cart'),
    path('cart/update-cart/', views.update_cart, name='update_cart'),
    path('load-view-cart/', load_view_cart, name='load_view_cart'),
    path('product-detail/<int:product_id>/',
         views.product_detail, name='product_detail'),
]
