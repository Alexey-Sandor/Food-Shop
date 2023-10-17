class Cart:
    """
    Класс для работы с корзиной пользователя.

    Атрибуты:

    - session - сессия пользователя
    - cart - словарь с данными о товарах в корзине

    Методы:

    - __getitem__, __setitem__ - доступ к корзине как к словарю
    - add_product - добавить товар в корзину
    - increase/decrease_product_amount - изменить количество товара
    - get_products - получить товары в корзине
    - clear - очистить корзину
    - get_total_price - получить общую стоимость
    """

    def __init__(self, request):
        """
        Устанавливает атрибуты текущей сессии пользователя,
        и пытается получить корзину из сессии.
        Если корзины нет, создаёт пустой словарь
        """
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def __getitem__(self, key):
        """
        Получает элемент корзины по ключу как из словаря.

        Аргументы:
        - key - ключ элемента корзины

        Возвращает:
        - Элемент корзины по указанному ключу
        """
        return self.cart[key]

    def __setitem__(self, key, value):
        """
        Устанавливает элемент в корзину по ключу как в словарь.

        Аргументы:
        - key - ключ элемента
        - value - значение элемента

        Сохраняет корзину после установки элемента.
        """
        self.cart[key] = value
        self.save()

    def save(self):
        """
        Сохраняет новое состояние корзины
        """
        self.session['cart'] = self.cart

    def add_product_to_cart(self, slug, name, price, weight, image):
        """
        Добавляет товар в корзину

        Аргументы:

        - slug - slug товара
        - name - имя товара
        - price - цена товара
        - weight - вес товара
        - image - изображение товара

        Если товара нет в корзине, в словаре корзины создается
        новая запись, где в качестве ключа выступает slug,
        а остальные поля являются значениями.

        Если товар уже есть в корзине, тогда вызывается метод который
        увеличит количество товара на 1, и к цене прибавится значение товара
        """
        if slug in self.cart:
            self.increase_product_amount(slug, price)
        else:
            self.cart[slug] = {
                'name': name,
                'price': price,
                'weight': weight,
                'image': image.url,
                'count': 1,
            }
        self.save()

    def increase_product_amount(self, slug, price):
        """
        Увеличивает количество и цену товара в корзине
        """
        self.cart[slug]['count'] += 1
        self.cart[slug]['price'] += price
        self.save()

    def decrease_product_amount(self, slug, price):
        """
        Уменьшает количество и цену товара в корзине если продукта более 1 шт.
        В противном случае удаляет товар из корзины
        """
        if self.cart[slug]['count'] > 1:
            self.cart[slug]['count'] -= 1
            self.cart[slug]['price'] -= price
            self.save()
        else:
            del self.cart[slug]
            self.save()

    def get_products(self):
        """
        Возвращает все продукты в корзине
        """
        return self.cart.items()

    def clear(self):
        """
        Очищает корзину
        """
        self.cart.clear()
        self.save()

    def get_total_price(self):
        """
        Возвращает общую сумму стоимости всех товаров в корзине
        """
        return sum((value['price']) for _, value in self.get_products())


def transfer_cart_on_login(request, anon_user_cart):
    """
    Переносит данные корзины из анонимной сессии в авторизованную при логине.

    Аргументы:

    - request - объект запроса
    - anon_user_cart - данные корзины анонимного пользователя

    Переносит товары из корзины анонимного пользователя в корзину
    авторизованного после логина.
    """
    if anon_user_cart:
        request.session['cart'] = anon_user_cart
    else:
        request.session.setdefault('cart', {})
    request.session.save()
