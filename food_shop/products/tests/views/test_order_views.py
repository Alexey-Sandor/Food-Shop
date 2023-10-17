from django.test import TestCase
from django.urls import reverse

from users.models import Client, BonusSystem


class OrderViewTestCase(TestCase):
    """
    Тест-кейс для функциональности представления заказа.
    """
    fixtures = ['users/fixtures/client.json', 'users/fixtures/address.json']

    def setUp(self):
        self.custom_client = Client.objects.get(id=1)
        self.backend = 'users.auth_backends.PhoneNumberBackend'

    def test_context_bonuses_amount(self):
        """
        Проверка, что контекст содержит правильное количество бонусов.
        """
        client_bonuses = BonusSystem.objects.get(profile_id=1)
        client_bonuses.bonuses_amount = 500
        client_bonuses.save()
        self.client.force_login(self.custom_client, backend=self.backend)
        response = self.client.get(reverse('products:create-order'))
        self.assertEqual(response.context.get('bonuses_count'), 500)
