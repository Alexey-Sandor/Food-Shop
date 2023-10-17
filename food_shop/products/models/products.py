from PIL import Image

from django.db import models
from django.urls import reverse


class Product(models.Model):
    """
    Модель товара.

    Поля:

    - name - название
    - description - описание
    - weight - вес
    - price - цена
    - image - изображение
    - category - категория
    - slug - url товара
    - available - доступность

    Методы:

    - __str__ - возвращает название продукта
    - save - обработка изображения до размера 300x300 перед сохранением
    - get_absolute_url - получить url товара
    """
    CATEGORY_CHOISES = (('pizza', 'Пицца'),
                        ('roll', 'Ролл'),
                        ('burger', 'Бургер'))

    name = models.CharField(verbose_name='Название продукта', unique=True,
                            max_length=50)
    description = models.TextField(verbose_name='Описание товара')
    weight = models.IntegerField(verbose_name='Вес товара')
    price = models.IntegerField(verbose_name='Цена товара')
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='products/')
    category = models.CharField(verbose_name='Категория товара',
                                choices=CATEGORY_CHOISES, max_length=50)
    slug = models.SlugField(max_length=100, verbose_name='url товара')
    available = models.BooleanField(verbose_name='Есть ли в наличии',
                                    default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        required_size = (300, 300)
        image.thumbnail(required_size)
        image.save(self.image.path)

    def get_absolute_url(self):
        return reverse('products:product-detail',
                       args=[self.slug])
