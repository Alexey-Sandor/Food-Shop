# Generated by Django 4.0 on 2023-08-15 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_address_client_address_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='users.profile', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='bonussystem',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonuses', to='users.profile', verbose_name='Пользователь'),
        ),
    ]