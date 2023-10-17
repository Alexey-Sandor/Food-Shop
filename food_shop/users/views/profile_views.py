from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from users.models import Profile


class ProfileView(LoginRequiredMixin, DetailView):
    """
    Представление детального просмотра профиля пользователя.

    Требует авторизации.

    Использует модель Profile.

    Делает выборку полей name, sex, orders_price_amount,
    bonuses__bonuses_amount
    с псевдонимом bonuses_amount.

    Возвращает объект профиля авторизованного пользователя
    """
    login_url = 'users:login'
    redirect_field_name = None
    template_name = 'users/profile.html'
    model = Profile

    def get_object(self, queryset=None):
        return self.model.objects.annotate(
            bonuses_amount=F('bonuses__bonuses_amount')).values(
            'name', 'sex', 'orders_price_amount', 'bonuses_amount').get(
            client=self.request.user)


class ProfieEditView(LoginRequiredMixin, UpdateView):
    """
    Представление для обновления информации профиля пользователя.

    Требует авторизации.

    Использует модель Profile.

    Возвращает объект профиля авторизованного пользователя
    """
    login_url = 'users:login'
    redirect_field_name = None
    model = Profile
    fields = ('name', 'sex', 'date_of_birthday')
    template_name = 'users/update_profile_info.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
