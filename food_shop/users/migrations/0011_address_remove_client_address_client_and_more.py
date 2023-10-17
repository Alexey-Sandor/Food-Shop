# Generated by Django 4.0 on 2023-07-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_client_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=20, verbose_name='Дом')),
                ('apartment_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Квартира')),
            ],
        ),
        migrations.RemoveField(
            model_name='client_address',
            name='client',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
    ]
