from users.models import BonusSystem, Profile
from users.tests.models.base_test_case_model import BaseTestCase


class BonusSystemTestCase(BaseTestCase):
    """Тесты модели Client.

    Тестируются:

    - строковое представление модели
    - verbose имена полей
    - методы модели

    Используется:

    - тестовый класс BaseTestCase и
    созданный им тестовый объект модели Client.
    - кастомный метод get_verbose_name
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.profile = Profile.objects.get(client=cls.custom_client)
        cls.bonus_system = BonusSystem.objects.get(profile=cls.profile)

    def test_obj_str_method(self):
        obj_name = self.bonus_system.id
        self.assertEqual(obj_name, 1)

    def test_obj_fields_verbose_name(self):
        field_data = [
            ('profile', 'Пользователь'),
            ('bonuses_amount', 'Количество бонусов'),
        ]
        for field_name, excepted_verbose_name in field_data:
            with self.subTest(msg=f'Ошибка проверки поля {field_name}'):
                actual_verbose_name = self.get_verbose_name(
                    self.bonus_system, field_name)
                self.assertEqual(actual_verbose_name, excepted_verbose_name)

    def test_add_bonuses(self):
        self.bonus_system.add_bonuses_amount(5000)
        self.assertEqual(self.bonus_system.bonuses_amount, 500)

        self.profile.orders_price_amount = 35000
        self.bonus_system.add_bonuses_amount(5000)
        self.assertEqual(self.bonus_system.bonuses_amount, 1000)

        self.profile.orders_price_amount = 50000
        self.bonus_system.add_bonuses_amount(5000)
        self.assertEqual(self.bonus_system.bonuses_amount, 1500)

    def test_decrease_bonuses(self):
        self.bonus_system.bonuses_amount = 1000
        self.bonus_system.decrease_bonuses_amount(200)
        self.assertEqual(self.bonus_system.bonuses_amount, 800)
