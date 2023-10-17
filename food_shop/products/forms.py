from django import forms

from products.models import Order
from users.models import Address


class OrderForm(forms.ModelForm):
    """Форма создания заказа"""
    client_address = forms.ModelChoiceField(
        queryset=None,
        help_text='город, улица, дом, номер квартиры',
        label='Адрес'
    )

    class Meta:
        model = Order
        exclude = ['profile', 'total_price',]

    def __init__(self, *args, **kwargs):
        """Инициализирует форму заказа.

        При инициализации ограничивает возможные адреса доставки
        только адресами данного пользователя.

        Аргументы:

        * args, kwargs - аргументы, передаваемые в базовый конструктор
        ModelsForm

        Ключевой аргумент:

        * user_profile - профиль пользователя, от имени которого
        создается заказ.

        Если задан аргумент user_profile:

        1. Извлекает его из kwargs

        2. Вызывает базовый конструктор ModelsForm

        3. Ограничивает queryset поля client_address только адресами данного
        пользователя.

        Это гарантирует, что в форме будут доступны для выбора только адреса
        данного пользователя.
        """
        user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)
        if user_profile is not None:
            self.fields['client_address'].queryset = Address.objects.filter(
                profile=user_profile)
