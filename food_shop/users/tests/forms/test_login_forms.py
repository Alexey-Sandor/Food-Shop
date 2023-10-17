from django.test import TestCase

from users.forms import PhoneNumberForm, CodeForm


class PhoneNumberFormTests(TestCase):

    def test_valid_form_data(self):
        """
        Проверяет валидность форм с допустимыми данными.
        """
        form_with_valid_data = [
            {'form': PhoneNumberForm,
             'data': {'phone_number': '+79997776655'}},
            {'form': CodeForm, 'data': {'code': '123456'}},
        ]
        for test_data in form_with_valid_data:
            form = test_data['form'](data=test_data['data'])
            with self.subTest(msg=f'Тест {test_data["form"]}'):
                self.assertTrue(form.is_valid())

    def test_invalid_form_data(self):
        """
        Проверяет невалидность форм с недопустимыми данными.
        """
        form_with_invalid_data = [
            {'form': PhoneNumberForm,
             'data': {'phone_number': '+79997fgfgfg'}},
            {'form': CodeForm, 'data': {'code': 'invalid'}},
        ]
        for test_data in form_with_invalid_data:
            form = test_data['form'](data=test_data['data'])
            with self.subTest(msg=f'Тест {test_data["form"]}'):
                self.assertFalse(form.is_valid())

    def test_form_field_placeholder(self):
        """
        Проверяет placeholder для полей номера телефона и кода.
        """
        form_data = [
            {'form': PhoneNumberForm, 'field': 'phone_number',
             'placeholder': 'Номер телефона'},
            {'form': CodeForm, 'field': 'code', 'placeholder': 'Код из SMS'}
        ]
        for test_data in form_data:
            form = test_data['form']()
            with self.subTest(f'Тест {test_data["form"]}'):
                self.assertEqual(
                    form.fields[test_data['field']].widget.attrs[
                        'placeholder'], test_data['placeholder'])

    def test_form_field_label(self):
        """
        Проверяет метки (labels) полей номера телефона и кода.
        """
        form_data = [
            {'form': PhoneNumberForm, 'field': 'phone_number',
             'label': 'Номер телефона'},
            {'form': CodeForm, 'field': 'code', 'label': 'Код'}
        ]
        for test_data in form_data:
            form = test_data['form']()
            with self.subTest(f'Тест {test_data["form"]}'):
                self.assertEqual(form.fields[test_data['field']].label,
                                 test_data['label'])