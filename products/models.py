from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

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
    image = models.ImageField(upload_to='product_images/')
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_valentines_special = models.BooleanField(default=False)
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
         Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    @property
    def total_price(self):
        if self.product.is_valentines_special:
            return self.quantity * self.product.discounted_price
        return self.quantity * self.product.price
# Create your models here.
