from django.shortcuts import render
from django.db.models import Q
from .models import Product, CATEGORY_CHOICES
from django.core.paginator import Paginator

def product_list(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', '')
    
    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category:
        products = products.filter(category=category)

    if sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'price_asc':
        products = products.order_by('price')

    paginator = Paginator(products, 16)  # Serve 16 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': page_obj,
        'CATEGORY_CHOICES': CATEGORY_CHOICES
    })