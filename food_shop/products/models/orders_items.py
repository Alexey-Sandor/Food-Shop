from django.db import models

from products.models.orders import Order
from products.models.products import Product


class OrderItem(models.Model):
    """
    Модель позиции заказа - связывает заказ и товар.

    Поля:

    - order - ссылка на заказ
    - product - ссылка на товар
    - product_total_price - общая цена товара в заказе
    - product_total_count - общее количество товара

    Методы:

    - __str__ - возвращает id объекта
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Номер заказа')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING,
                                verbose_name='Номер товара')
    product_total_price = models.IntegerField(
        verbose_name='Общая цена товара одной позиции в заказе')
    product_total_count = models.IntegerField(
        verbose_name='Общее количество товара одной позиции в заказе')

    def __str__(self):
        return self.id
