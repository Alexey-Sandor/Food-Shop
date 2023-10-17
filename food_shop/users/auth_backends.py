from django.contrib.auth.backends import BaseBackend

from users.models import Client


class PhoneNumberBackend(BaseBackend):
    """Бэкенд аутентификации по номеру телефона."""
    def authenticate(self, phone_number=None):
        try:
            user = Client.objects.get(phone_number=phone_number)
            return user
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.only('id').get(pk=user_id)
        except Client.DoesNotExist:
            return None
