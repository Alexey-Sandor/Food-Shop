from django.db import models


class Client(models.Model):
    """Модель пользователя.

    Поля:

    - phone_number - номер телефона
    - last_login - дата и время последнего входа

    Строковое представление содержит телефон пользователя.

    Предоставляет свойство is_authenticated для системы аутентификации.
    """
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    last_login = models.DateTimeField(verbose_name='Дата последнего входа',
                                      null=True, blank=True)

    def __str__(self):
        return self.phone_number

    @property
    def is_authenticated(self):
        return True
