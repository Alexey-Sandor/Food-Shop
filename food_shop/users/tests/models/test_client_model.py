from users.tests.models.base_test_case_model import BaseTestCase


class ClientModelTestCase(BaseTestCase):
    """Тесты модели Client.

    Тестируются:

    - строковое представление модели
    - verbose имена полей

    Используется:

    - тестовый класс BaseTestCase и
    созданный им тестовый объект модели Client.
    - кастомный метод get_verbose_name
    """

    def test_obj_str_method(self):
        obj_name = str(self.custom_client)
        self.assertEqual(obj_name, '+79780000000')

    def test_obj_fields_verbose_name(self):
        field_data = [
            ('phone_number', 'Телефон'),
            ('last_login', 'Дата последнего входа'),
        ]

        for field_name, expected_verbose_name in field_data:
            with self.subTest(msg=f'ошибка проверки поля {field_name}'):
                actual_verbose_name = self.get_verbose_name(
                    self.custom_client, field_name)
                self.assertEqual(actual_verbose_name, expected_verbose_name)
