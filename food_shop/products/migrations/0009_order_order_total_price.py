# Generated by Django 4.0 on 2023-07-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_total_price',
            field=models.IntegerField(default=1000, verbose_name='Итоговая цена заказа'),
            preserve_default=False,
        ),
    ]
