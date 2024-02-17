from django.shortcuts import render
import json
from django.http import JsonResponse
from django.db.models import Q
from .models import Product, CATEGORY_CHOICES
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, Cart, CartItem
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

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, quantity_remaining__gt=0)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        product.quantity_remaining -= 1  # Decrement the product's available quantity
        product.save()

    # Calculate the total number of individual items in the cart
    cart_items_total_quantity = sum(item.quantity for item in cart.items.all())
    return JsonResponse({'cartItemsCount': cart_items_total_quantity})

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})

# views.py
@login_required
def cart_items(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'products/cart_items.html', {'cart': cart})
@login_required
@require_POST
def remove_from_cart(request):
    data = json.loads(request.body)
    item_id = data.get('itemId')
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    cart_item.product.quantity_remaining += cart_item.quantity
    cart_item.product.save()
    cart_item.delete()

    cart = Cart.objects.get(user=request.user)
    return JsonResponse({
        'status': 'success',
        'cartTotal': cart.total_price,
        'cartItemsCount': cart.items.count()
    })

@login_required
@require_POST
def update_cart(request):
    data = json.loads(request.body)
    item_id = data.get('itemId')
    action = data.get('action')
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product = cart_item.product

    if action == "increase":
        if product.quantity_remaining > 0:
            cart_item.quantity += 1
            product.quantity_remaining -= 1
        else:
            return JsonResponse({'status': 'no_stock'})

    elif action == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            product.quantity_remaining += 1
        else:
            cart_item.delete()  # If quantity is 1, remove the item

    product.save()
    cart_item.save()

    cart = Cart.objects.get(user=request.user)
    return JsonResponse({
        'status': 'success',
        'itemQuantity': cart_item.quantity,
        'itemTotal': cart_item.total_price,
        'cartTotal': cart.total_price,
        'cartItemsCount': cart.items.count()
    })
@login_required
def load_view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'products/view_cart_content.html', {'cart': cart})

def checkout(request):
    # Your checkout logic here
    return render(request, 'checkout.html')