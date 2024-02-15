# Generated by Django 5.0.2 on 2024-02-15 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('flowers', 'Flowers'), ('chocolate', 'Chocolate'), ('jewellery', 'Jewellery'), ('hand_crafted', 'Hand Crafted'), ('original', 'Original'), ('cards', 'Cards'), ('decorations', 'Decorations')], max_length=50)),
                ('quantity_remaining', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]