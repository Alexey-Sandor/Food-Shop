from django.db import models

from users.models import Address, Profile


class Order(models.Model):
    """
    Модель заказа.

    Поля:

    - profile - ссылка на профиль
    - client_name - имя получателя
    - client_phone_number - телефон получателя
    - client_addressce - ссылка на адрес
    - total_price - общая сумма заказа
    - bonuses_was_used - количетсво использованных бонусов

    Методы:
    - __str__ - возвращает id
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        verbose_name='Пользователь сделавший заказ')
    client_name = models.CharField(
        verbose_name='Имя получателя', max_length=25)
    client_phone_number = models.CharField(
        verbose_name='Номер телефона получателя', max_length=25)
    client_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING,
                                       verbose_name='Адрес пользователя')
    total_price = models.IntegerField(verbose_name='Итоговая цена заказа')
    bonuses_was_used = models.IntegerField(
        verbose_name='Сколько использовано бонусов', default=0)

    def __str__(self):
        return self.id
