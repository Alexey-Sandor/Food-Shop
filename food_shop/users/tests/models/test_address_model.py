from django.core.management import call_command

from users.models import Address, Profile
from users.tests.models.base_test_case_model import BaseTestCase

class AddressModelTestCase(BaseTestCase):
    """Тесты модели Address.

    Тестируются:

    - строковое представление модели
    - verbose имена полей

    Использует:

    - тестовый класс BaseTestCase
    - два созданных объекта модели Address
    - кастомный метод get_verbose_name
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'address.json')
        cls.profile = Profile.objects.get(client=cls.custom_client)
        cls.address_without_appartment = Address.objects.get(id=1)
        cls.address_with_appartment = Address.objects.get(id=2)

    def test_obj_str_method(self):
        with self.subTest(msg='Тест адреса без номера квартиры'):
            obj_name_without_appartment = str(self.address_without_appartment)
            self.assertEqual(obj_name_without_appartment,
                             'Москва, Пушкина, 13')

        with self.subTest(msg='Тест адреса с номером квартиры'):
            obj_name_with_appartment = str(self.address_with_appartment)
            self.assertEqual(obj_name_with_appartment,
                             'Москва, Пушкина, 13, 120')

    def test_obj_fields_verbose_name(self):
        field_data = [
            ('profile', 'Профиль пользователя'),
            ('city', 'Город'),
            ('street', 'Улица'),
            ('house_number', 'Дом'),
            ('apartment_number', 'Квартира')
        ]
        for field_name, excepted_verbose_name in field_data:
            with self.subTest(msg=f'Ошибка проверки поля {field_name}'):
                actual_verbose_name = self.get_verbose_name(
                    self.address_with_appartment, field_name)
                self.assertEqual(actual_verbose_name, excepted_verbose_name)
