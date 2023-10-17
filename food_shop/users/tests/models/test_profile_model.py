from users.models import Profile, Client
from users.tests.models.base_test_case_model import BaseTestCase


class ProfileTestCase(BaseTestCase):
    """Тесты модели Profile.

    Тестируются:

    - строковое представление модели
    - verbose имена полей
    - метод модели

    Используется:

    - тестовый класс BaseTestCase и
    созданный им тестовый объект модели Client.
    - кастомный метод get_verbose_name
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.profile = Profile.objects.get(client__phone_number='+79780000000')

    def test_obj_str_method(self):
        obj_name = self.profile.id
        self.assertEqual(obj_name, 1)

    def test_obj_fields_verbose_name(self):
        field_data = [
            ('client', 'Пользователь'),
            ('name', 'Имя'),
            ('sex', 'Пол'),
            ('date_of_birthday', 'Дата рождения'),
            ('orders_price_amount', 'Общая сумма заказов'),
        ]
        for field_name, excepted_verbose_name in field_data:
            with self.subTest(msg=f'Ошибка проверки поля {field_name}'):
                actual_verbose_name = self.get_verbose_name(
                    self.profile, field_name)
                self.assertEqual(actual_verbose_name, excepted_verbose_name)

    def test_order_price_amout(self):
        self.profile.update_orders_price_amount(500)
        self.assertEqual(self.profile.orders_price_amount, 500)
