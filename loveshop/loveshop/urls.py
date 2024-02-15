from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),  # Home page
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs
    path('accounts/register/', TemplateView.as_view(template_name="registration/register.html"), name='register'),  # Placeholder for registration
    path('products/', include('products.urls', namespace='products')),  # Products app
    path('contact/', include('contact.urls', namespace='contact')),  # Contact app
    path('checkout/', include('checkout.urls', namespace='checkout')),  # Checkout app
]