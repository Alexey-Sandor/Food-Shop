from django.test import TestCase
from django.core.management import call_command

from products.forms import OrderForm
from users.models import Address, Profile


class FormTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        call_command('loaddata', 'users/fixtures/client.json',
                     'users/fixtures/address.json')
        cls.user_profile_with_addresses = Profile.objects.get(id=1)
        cls.fixture_adresses = Address.objects.all()
        cls.user_profile_without_addresses = Profile.objects.get(id=2)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_sees_his_addresses(self):
        form = OrderForm(user_profile=self.user_profile_with_addresses)
        self.assertEqual(list(form.fields['client_address'].queryset),
                         list(self.fixture_adresses)[::-1])

    def test_user_dont_sees_other_users_addresses(self):
        form = OrderForm(user_profile=self.user_profile_without_addresses)
        self.assertEqual(list(form.fields['client_address'].queryset), [])
