from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity_remaining', 'rating']
    list_filter = ['category', 'rating']
    search_fields = ['name', 'description']