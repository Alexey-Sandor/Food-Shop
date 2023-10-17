from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import Address


class CreateAddress(LoginRequiredMixin, CreateView):
    """
    Представление для созданий адреса доставки пользователя.

    Требует авторизации.

    Использует модель Address.

    Добавить адрес можно на странице оформления заказа, после чего происходит
    редирект обратно к оформлению заказа

    После проверки валидности формы, автоматически подставляет профиль текущего
    пользователя в связанное поле profile
    """
    redirect_field_name = None
    login_url = 'users:login'
    model = Address
    fields = ('city', 'street', 'house_number', 'apartment_number')
    template_name = 'users/add_address.html'
    success_url = reverse_lazy('products:create-order')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
