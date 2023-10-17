from django.core.management import call_command
from django.test import TestCase

from users.models import Client


class BaseTestCase(TestCase):
    # """Базовый класс для тестов моделей.

    # Содержит:

    # - метод setUpClass для создания тестового пользователя
    # - метод tearDownClass для очистки бд

    # - вспомогательный метод get_verbose_name для получения
    # verbose имени поля модели

    # Наследуется тестами конкретных моделей.
    # """

    @classmethod
    def setUpClass(cls):
        call_command('loaddata', 'client.json')
        cls.custom_client = Client.objects.get(phone_number='+79780000000')

    @classmethod
    def tearDownClass(cls):
        pass

    def get_verbose_name(self, model_obj, field_name):
        return model_obj._meta.get_field(field_name).verbose_name