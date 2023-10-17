from django.db import models

from users.models import Client


class Profile(models.Model):
    """Модель профиля пользователя.

    Поля:

    - client - ссылка на модель пользователя
    - name - Имя пользователя
    - sex - Пол пользователя
    - date_of_birthday - День рождения пользователя
    - orders_price_amount - Сумма заказов пользователя

    Методы:

    - __str__ - возвращает id объекта
    - update_orders_price_amount - обновляет общую сумму заказов пользователя
    """
    SEX_CHOISES = (('male', 'мужской'),
                   ('female', 'женский'))
    client = models.OneToOneField(Client, on_delete=models.CASCADE,
                                  verbose_name='Пользователь')
    name = models.CharField(verbose_name='Имя', max_length=50,
                            blank=True, null=True)
    sex = models.CharField(verbose_name='Пол', max_length=10,
                           choices=SEX_CHOISES, default='Не указан')
    date_of_birthday = models.DateField(verbose_name='Дата рождения',
                                        blank=True, null=True)
    orders_price_amount = models.IntegerField(
        verbose_name='Общая сумма заказов', default=0)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.id

    def update_orders_price_amount(self, order_price):
        """
        обновляет общую сумму заказов пользователя
        """
        self.orders_price_amount += order_price
        self.save()
