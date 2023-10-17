
from users.models import Profile


def process_bonuses_calculation(cart, form, user):
    """
    Логика обработки бонусов при заказа.

    Аргументы:
    cart - экземпляр корзины
    form - заполненная форма заказа
    user - текущий пользователь

    Если бонусы были использованы, высчитываем стоимость заказа
    с учетом бонусов, отнимает эти бонусы у пользователя и обновляем
    значение общей сумму заказов.
    Если бонусы не были использованы, просто обновляем общую сумму заказов
    """
    bonuses_used = form.cleaned_data['bonuses_was_used']
    profile = Profile.objects.select_related('bonuses').get(client=user)

    if bonuses_used > 0:
        profile.bonuses.decrease_bonuses_amount(bonuses_used)
        total_price = cart.get_total_price() - bonuses_used
    else:
        total_price = cart.get_total_price()

    form.instance.profile = profile
    form.instance.total_price = total_price
    profile.bonuses.add_bonuses_amount(total_price)
    profile.update_orders_price_amount(total_price)
