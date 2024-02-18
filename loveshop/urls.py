from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"),
         name='home'),  # Home page
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls', namespace='products')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('about/', include('about.urls')),
]
