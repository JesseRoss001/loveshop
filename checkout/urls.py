# checkout/urls.py
from django.urls import path
from .views import checkout_page, create_checkout_session, payment_success, payment_cancel, review_order

urlpatterns = [
    path('', checkout_page, name='checkout'),
    path('review-order/', review_order, name='review_order'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('success/', payment_success, name='success'),
    path('cancel/', payment_cancel, name='cancel'),
]