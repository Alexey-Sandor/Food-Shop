from django import forms
from django.core.validators import RegexValidator

from users.models import Client


class PhoneNumberForm(forms.ModelForm):
    """Форма для ввода номера телефона пользователя.

    Форма состоит из одного поля phone_number, в которое пользователь
    вводит номер телефона в формате: +79999999999

    Валидация поля:
    - Номер должен начинаться с + и содержать только цифры
    - Длина номера - 12 символов

    При успешной валидации в представлении создаётся или получается объект
    модели Client с введенным номером телефона.
    """
    phone_number = forms.CharField(
        min_length=12, max_length=12,
        label='Номер телефона',
        widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
        validators=[RegexValidator(r'^\+7\d{10}$',
                                   'Номер должен содержать только цифры')])

    class Meta:
        model = Client
        fields = ['phone_number']


class CodeForm(forms.Form):
    """Форма для ввода SMS-кода для авторизации.

    Состоит из одного поля code, куда пользователь вводит код из SMS.

    Валидация поля:
    - Длина кода - 6 цифр
    - Разрешены только цифры

    Форма не сохраняет данные в модель, а лишь
    валидирует корректность введенного кода.
    """
    code = forms.CharField(
        min_length=6, max_length=6,
        label='Код', required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Код из SMS'}),
        validators=[RegexValidator(r'^\d+$',
                                   'Код должен содержать только цифры')])
