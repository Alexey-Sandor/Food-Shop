# Generated by Django 4.0 on 2023-07-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_only_pizza_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='only_pizza_size',
        ),
    ]
