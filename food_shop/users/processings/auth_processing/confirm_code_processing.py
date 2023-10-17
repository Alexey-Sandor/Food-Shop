from django.contrib.auth import login
from django.shortcuts import redirect, render

from products.cart import transfer_cart_on_login
from users.models import Client


def confirm_code(request, form):
    """Подтверждает код и авторизует пользователя если код верный.

    Проверяет, что код из формы совпадает с кодом в сессии.
    Если да, авторизует пользователя или создает нового, а текже
    переносит корзину пользователя в новую сесию
    Если нет - показывает ошибку в форме.
    """
    code = form.cleaned_data['code']
    session_code = request.session.get('code')
    if code == session_code:
        phone_number = request.session['phone_number']
        user, created = Client.objects.get_or_create(
            phone_number=phone_number)
        login(request, user, backend='users.auth_backends.PhoneNumberBackend')
        transfer_cart_on_login(
            request, request.session.get('cart'))
        del request.session['code']
        del request.session['phone_number']
        return redirect('users:profile')
    else:
        form.add_error('code', 'Введенный код указан неверно')
        return render(request, 'users/enter_code.html', {'form': form})
