from django.test import TestCase
from django.urls import reverse

from products.models import Product


class CartViewTestCase(TestCase):
    fixtures = ['product']

    def setUp(self):
        self.product = Product.objects.get(id=1)
        self.cart_url = reverse('products:add_to_cart',
                                kwargs={'slug': self.product.slug})
        self.increase_url = reverse('products:increase-count',
                                    kwargs={'slug': self.product.slug})
        self.decrease_url = reverse('products:decrease-count',
                                    kwargs={'slug': self.product.slug})

    def test_add_product_to_cart(self):
        """
        Проверка, что добавление продукта в корзину работает корректно.
        """
        self.client.post(self.cart_url)
        self.assertIn(self.product.slug, self.client.session['cart'])

    def test_increase_and_decrease_product_amount(self):
        """
        Проверка, что увеличение и уменьшение количества продукта
        в корзине работает корректно.
        """
        self.client.post(self.cart_url)
        self.client.post(self.increase_url)
        self.assertEqual(
            self.client.session['cart'][self.product.slug]['count'], 2)

        self.client.post(self.decrease_url)
        self.assertEqual(
            self.client.session['cart'][self.product.slug]['count'], 1)

        self.client.post(self.decrease_url)
        self.assertEqual(self.client.session['cart'], {})

    def test_clear_cart(self):
        """
        Проверка, что очистка корзины работает корректно.
        """
        self.client.post(self.cart_url)
        self.assertEqual(
            self.client.session['cart'][self.product.slug]['count'], 1)
        self.client.post(reverse('products:cart-clear'))
        self.assertEqual(self.client.session['cart'], {})
