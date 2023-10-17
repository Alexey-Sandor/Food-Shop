from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from products.cart import Cart
from products.forms import OrderForm
from products.processings import (create_order_and_order_items,
                                  process_bonuses_calculation)
from users.models import BonusSystem


class OrderView(LoginRequiredMixin, CreateView):
    """Представление для создания заказа пользователем.

    Атрибуты:

    - login_url - URL для редиректа при неавторизованном пользователе
    - form_class - используемая форма заказа
    - template_name - шаблон для отображения формы
    - success_url - URL для редиректа при успешном создании заказа

    Методы:

    - get_context_data:
        Добавляет в контекст данные о корзине и бонусах пользователя

    - get_form_kwargs:
        Передает профиль пользователя в форму для фильтрации адресов

    - form_valid:
        Создает заказ из данных формы и корзины
        Обрабатывает использование бонусов
        Перенаправляет на страницу успешного создания
    """
    login_url = 'users:login'
    form_class = OrderForm
    template_name = 'products/order_create.html'
    success_url = reverse_lazy('products:order-success-created')

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст данные о товаре в корзине,
        количестве бонусов пользователя и общую сумму товаров.
        """
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['bonuses_count'] = BonusSystem.objects.get(
            profile=self.request.user.profile).bonuses_amount
        context['items_in_cart'] = cart.get_products()
        context['total_price'] = cart.get_total_price()
        return context

    def get_form_kwargs(self):
        """
        Передает профиль пользователя в форму для фильтрации адресов.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user_profile'] = self.request.user.profile
        return kwargs

    def form_valid(self, form):
        """
        Создает заказ из данных формы и корзины.
        Обрабатывает использование бонусов.
        Перенаправляет на страницу успешного создания заказа.
        """
        cart = Cart(self.request)
        process_bonuses_calculation(cart, form, self.request.user)
        create_order_and_order_items(cart, form)
        return super().form_valid(form)
