# Generated by Django 4.0 on 2023-08-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
    ]
