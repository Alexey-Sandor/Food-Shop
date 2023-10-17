from products.models import OrderItem, Product


def create_order_and_order_items(cart, form):
    """Создает заказ из формы и позиции заказа из корзины.

    Аргументы:
    cart - экземпляр корзины
    form - заполненная форма заказа

    Создает заказ на основе данных формы,
    а также позиции заказа на основе продуктов в корзине.
    После создания очищает корзину.
    """
    order = form.save()
    order_items = [
        OrderItem(
            order=order,
            product=Product.objects.get(slug=item_slug),
            product_total_price=item_data['price'],
            product_total_count=item_data['count']
        )
        for item_slug, item_data in cart.get_products()
    ]
    OrderItem.objects.bulk_create(order_items)
    cart.clear()
