from django.db import models

from users.models import Profile


class Address(models.Model):
    """Модель для хранения адреса пользователя.

    Поля:

    - client - внешний ключ на модель Пользователь
    - city - город
    - street - улица
    - house_number - номер дома
    - apartment_number - номер квартиры (необязательно)

    Строковое представление содержит поля:
    город, улица, номер дома, номер квартиры (необязательно).
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                verbose_name='Профиль пользователя',
                                related_name='addresses')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Дом')
    apartment_number = models.CharField(max_length=20, verbose_name='Квартира',
                                        blank=True, null=True)

    def __str__(self):
        apartment_str = (f', {self.apartment_number}'
                         if self.apartment_number is not None else '')
        return (f'{self.city}, {self.street},'
                f' {self.house_number}{apartment_str}')
