from django.test import TestCase
from django.urls import reverse

from users.models import Client


class UrlsTestCase(TestCase):
    """Тесты доступа к различным страницам в зависимости от пользователя.

    Проверяется доступ и редиректы для страниц приложения для:

    - анонимных пользователей
    - авторизованных пользователей
    - пользователей с session данными

    Используются:

    - кастомный класс для аутентификации по номеру телефона
    - созданный тестовый клиент
    - проверки статус кодов и шаблонов ответов
    - вспомогательный метод для проверки редиректов
    """
    fixtures = ['client']

    def setUp(self):
        self.backend = 'users.auth_backends.PhoneNumberBackend'
        self.custom_client = Client.objects.get(phone_number='+79780000000')

    def check_redirect(self, urls, message, url_for_reverse):
        for url in urls:
            with self.subTest(msg=f'{message} {url}'):
                response = self.client.get(reverse(url))
                self.assertRedirects(response, reverse(url_for_reverse))

    def test_redirect_anon_user_from_pages(self):
        urls = ('users:logout', 'users:profile', 'users:add-address')
        self.check_redirect(urls, 'Тест редиректа анонимного юзера с',
                            'users:login')

    def test_redirect_auth_user_from_pages(self):
        urls = ('users:login', 'users:confirm', 'users:resend_code')
        self.client.force_login(self.custom_client, backend=self.backend)
        self.check_redirect(urls, 'Тест редиректа авторизованного юзера с',
                            'users:profile')

    def test_redirect_user_without_session_data_from_pages(self):
        urls = ('users:confirm', 'users:resend_code')
        self.check_redirect(urls,
                            ('Тест редиректа юзера без номера телефона '
                             'и кода в сессии с'),
                            'users:login')

    def test_pages_for_any_user(self):
        response = self.client.get(reverse('users:privacy-policy'))
        self.assertTemplateUsed(response, 'users/privacy_policy.html')
        self.assertEqual(response.status_code, 200)
        self.client.force_login(self.custom_client, backend=self.backend)

        response_for_auth_user = self.client.get(
            reverse('users:privacy-policy'))
        self.assertEqual(response_for_auth_user.status_code, 200)

    def test_pages_for_auth_user(self):
        urls_templates_status_codes = [
            ('users:profile', 'users/profile.html', 200),
            ('users:add-address', 'users/add_address.html', 200),
        ]
        self.client.force_login(self.custom_client, backend=self.backend)
        for url, template, code_status in urls_templates_status_codes:
            with self.subTest(msg=f'Тест доступа к адресу: {url}'):
                response = self.client.get(reverse(url))
                self.assertTemplateUsed(response, template)
                self.assertEqual(response.status_code, code_status)

    def test_pages_for_anon_user(self):
        response = self.client.get(reverse('users:login'))
        self.assertTemplateUsed(response, 'users/enter_phone_number.html')
        self.assertEqual(response.status_code, 200)

    def test_pages_with_session_data(self):
        urls_templates_status_codes = [
            ('users:confirm', 'users/enter_code.html', 200),
            ('users:resend_code', None, 200)
        ]
        session_data = self.client.session
        session_data['code'] = '123456'
        session_data['phone_number'] = '+79781111111'
        session_data.save()
        for url, template, status_code in urls_templates_status_codes:
            with self.subTest(msg=f'Тест url {url}'):
                response = self.client.get(reverse(url))
                if template is not None:
                    self.assertTemplateUsed(response, template)
                self.assertEqual(response.status_code, status_code)
