from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'description',
                    'price', 'category')
    prepopulated_fields = {'slug': ('name',)}
