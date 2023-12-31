# Generated by Django 4.0 on 2023-07-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bonuses_amount',
            field=models.IntegerField(default=0, verbose_name='Количестко бонусов'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='orders_price_amount',
            field=models.IntegerField(default=0, verbose_name='Общая сумма заказов'),
        ),
    ]
