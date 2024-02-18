from django.contrib import admin
from .models import Product, Cart, CartItem


# Existing ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price',
        'quantity_remaining', 'rating', 'is_valentines_special']
    list_filter = ['category', 'rating']
    search_fields = ['name', 'description']


# New admin registration for Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username']


# New admin registration for CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
    list_filter = ['cart']
    search_fields = ['cart__user__username', 'product__name']
