from django.test import TestCase
from django.urls import reverse

from users.models import Client


class AuthTests(TestCase):

    """Тесты процесса авторизации пользователей."""

    def setUp(self):
        self.phone_number = '+79780000341'
        self.code = '123456'

        self.session = self.client.session
        self.session['phone_number'] = self.phone_number
        self.session['code'] = self.code
        self.session.save()

    def test_if_code_valid_create_new_user(self):
        """
        При вводе верного кода для нового пользователя
        создается учетная запись.
        """
        self.assertEqual(Client.objects.count(), 2)

        self.client.post(reverse('users:confirm'), {'code': self.code})

        self.assertEqual(Client.objects.count(), 3)

    def test_valid_code_existing_user(self):
        """
        При вводе верного кода для существующего пользователя
        новый пользователь не создается.
        """
        Client.objects.create(phone_number=self.phone_number)
        count = Client.objects.count()

        self.client.post(reverse('users:confirm'), {'code': self.code})
        self.assertEqual(Client.objects.count(), count)

    def test_invalid_code(self):
        """При неверном коде выдается ошибка."""
        response = self.client.post(reverse('users:confirm'),
                                    {'code': '654321'})

        self.assertFormError(response, 'form', 'code',
                             'Введенный код указан неверно')

    def test_session_cleaned_on_auth(self):
        """После авторизации номер телефона и код удаляются из сессии,
        а корзина сохраняется"""
        self.assertIn('phone_number', self.session)
        self.assertIn('code', self.session)
        self.session['cart'] = 'Test product'
        self.session.save()
        self.client.post(reverse('users:confirm'), {'code': self.code})
        self.session = self.client.session
        self.assertNotIn('phone_number', self.session)
        self.assertNotIn('code', self.session)
        self.assertIn('cart', self.session)


class LogoutTests(TestCase):
    fixtures = ['client']
    """Тесты разлогинивания пользователей."""

    def test_cart_saved_after_logout(self):
        """После разлогинивания корзина сохраняется в сессии."""
        user = Client.objects.get(phone_number='+79780000000')
        self.client.force_login(user)
        self.session = self.client.session
        self.session['cart'] = 'Test product'
        self.session.save()

        self.client.get(reverse('users:logout'))
        self.assertIn('cart', self.session)
