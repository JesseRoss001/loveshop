from django.shortcuts import render
  # Import your Product model

def product_list(request):
     # Query all products
    return render(request, 'products/product_list.html', {})

# Create your views here.
