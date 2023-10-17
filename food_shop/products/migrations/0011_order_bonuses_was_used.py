# Generated by Django 4.0 on 2023-07-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_order_total_price_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bonuses_was_used',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default=20, verbose_name='Сколько использовано бонусов'),
            preserve_default=False,
        ),
    ]