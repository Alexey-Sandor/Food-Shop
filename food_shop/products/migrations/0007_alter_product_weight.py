# Generated by Django 4.0 on 2023-07-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(verbose_name='Вес товара'),
        ),
    ]
