from decimal import Decimal

from django.db import models

from users.models import Profile


class BonusSystem(models.Model):
    """
    Модель для хранения информации о бонусах пользователя.

    Поля:

    - profile - ссылка на профиль пользователя
    - bonuses_amount - количество бонусов пользователя

    Методы:

    - __str__ - возвращает id объекта
    - add_bonuses_amount - начисляет бонусы на основе стоимости заказа
    - decrease_bonuses_amount - списывает количество используемых бонусов
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   verbose_name='Пользователь',
                                   related_name='bonuses')
    bonuses_amount = models.IntegerField(verbose_name='Количество бонусов',
                                         default=0)

    def __str__(self):
        return self.id

    def add_bonuses_amount(self, order_price):
        """
        Yачисляет бонусы на основе стоимости заказа
        """
        if self.profile.orders_price_amount <= 30000:
            self.bonuses_amount += order_price * Decimal('0.10')
        elif self.profile.orders_price_amount <= 45000:
            self.bonuses_amount += order_price * Decimal('0.20')
        self.save()

    def decrease_bonuses_amount(self, count_bonuses_was_used):
        """
        Cписывает количество используемых бонусов
        """
        self.bonuses_amount -= count_bonuses_was_used
        self.save()
