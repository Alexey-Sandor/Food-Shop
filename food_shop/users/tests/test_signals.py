from django.test import TestCase
from users.models import Client, Profile, BonusSystem


class CreateUserProfileAndBonusSystemTest(TestCase):
    fixtures = ['client']
    """Тесты для сигналов создания профиля и системы бонусов пользователя"""

    def test_profile_created(self):
        """Проверка, что при создании пользователя создается его профиль
        и система бонусов"""
        user = Client.objects.get(phone_number='+79780000000')
        self.assertEqual(Profile.objects.count(), 2)
        self.assertEqual(Profile.objects.first().client, user)
        profile = Profile.objects.first()
        self.assertEqual(profile.client, user)
        self.assertEqual(BonusSystem.objects.count(), 2)
        self.assertEqual(BonusSystem.objects.first().profile, profile)
