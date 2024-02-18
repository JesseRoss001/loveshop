from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path(
        '', views.contact_page, name='index'),
    path('contact_success/', views.contact_success, name='contact_success'),
]
