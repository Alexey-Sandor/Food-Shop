from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import CodeForm, PhoneNumberForm
from users.processings import confirm_code, send_code_at_form_valid
from users.tasks import send_confirmation_code_task
from users.utils import generate_confirmation_code


class EnterPhoneNumberView(FormView):
    """Представление для ввода номера телефона.

    Отправляет код подтверждения после валидации формы.
    Перенаправляет авторизованных пользователей на профиль.
    """
    form_class = PhoneNumberForm
    template_name = 'users/enter_phone_number.html'
    success_url = reverse_lazy('users:confirm')

    def form_valid(self, form):
        print('hello')
        send_code_at_form_valid(self.request, form)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().dispatch(request, *args, **kwargs)


class EnterCodeView(FormView):
    """Представление для ввода кода подтверждения.

    Проверяет наличие номера и кода в сессии.
    Перенаправляет  пользователей без этих данных в сессии
    на страницу ввода номера телефона.
    Перенаправляет авторизованных пользователей на профиль.
    Вызывает confirm_code для авторизации при валидной форме.

    """
    form_class = CodeForm
    template_name = 'users/enter_code.html'
    sucess_url = reverse_lazy('users:profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        if not ('phone_number' in request.session
                and 'code' in request.session):
            return redirect('users:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return confirm_code(self.request, form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone_number = self.request.session['phone_number']
        context['phone_number'] = '+7 {} {} {} {}'.format(
            phone_number[2:5], phone_number[5:8],
            phone_number[8:10], phone_number[10:12])
        return context


def resend_code(request):
    """Отправляет повторный код подтверждения на номер из сессии.

    Доступно только для неавторизованных пользователей
    с номером и кодом в сессии.
    Перенаправляет авторизованных пользователей на профиль.
    Перенаправляет  пользователей без кода и номера в сессии
    на страницу ввода номера телефона.
    """
    if request.user.is_authenticated:
        return redirect('users:profile')
    if not ('phone_number' in request.session and 'code' in request.session):
        return redirect('users:login')
    code = generate_confirmation_code()
    phone_number = request.session['phone_number']
    send_confirmation_code_task.delay(phone_number, code)
    request.session['code'] = code
    return HttpResponse('code resend')


@login_required(login_url='users:login', redirect_field_name=None)
def logout_user(request):
    """Выход пользователя из системы.

    Сохраняет данные корзины в сессии после разлогинивания.
    """
    cart_data = request.session.get('cart')
    logout(request)
    request.session['cart'] = cart_data
    return redirect('products:home')
