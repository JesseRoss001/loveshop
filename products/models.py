from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Define the category choices
CATEGORY_CHOICES = (
    ('flowers', 'Flowers'),
    ('chocolate', 'Chocolate'),
    ('jewellery', 'Jewellery'),
    ('hand_crafted', 'Hand Crafted'),
    ('original', 'Original'),
    ('cards', 'Cards'),
    ('decorations', 'Decorations'),
)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity_remaining = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='product_images/')  # Assuming you have media set up
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name
# Create your models here.
