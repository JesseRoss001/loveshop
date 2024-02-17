# checkout/views.py
import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddressForm
from accounts.models import UserProfile
from django.http import JsonResponse,HttpResponse
from products.models import Cart, CartItem  # Ensure these are correctly imported

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout_page(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            # Redirect to Stripe Checkout
            return redirect('checkout:create_checkout_session')
    else:
        form = AddressForm(instance=user_profile)

    return render(request, 'checkout/checkout_page.html', {'form': form})



stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    try:
        user_cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=user_cart)

        if not cart_items:
            return HttpResponse("Your cart is empty.", status=404)

        line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100),
            },
            'quantity': item.quantity,
        } for item in cart_items]

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/'),
            cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        )

        return redirect(checkout_session.url, code=303)
    except Cart.DoesNotExist:
        return HttpResponse("You do not have a cart.", status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)})

