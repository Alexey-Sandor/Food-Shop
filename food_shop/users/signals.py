from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import Client, Profile, BonusSystem


@receiver(post_save, sender=Client)
def create_user_profile(sender, instance, created, **kwargs):
    """Создает профиль для нового пользователя после его создания.

    Вызывается сигналом post_save для модели Client.
    """
    if created:
        Profile.objects.create(client=instance)


@receiver(post_save, sender=Profile)
def create_bonus_system_for_user(sender, instance, created, **kwargs):
    """Создает систему бонусов для профиля пользователя после его создания.

    Вызывается сигналом post_save для модели Profile.
    """
    if created:
        BonusSystem.objects.create(profile=instance)
