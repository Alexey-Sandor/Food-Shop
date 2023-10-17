from django.test import TestCase
from django.urls import reverse
from products.models import Product
from users.models import Client
from django.core.management import call_command


class UrlsTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        call_command('loaddata', 'product', 'users/fixtures/client.json')
        cls.product = Product.objects.get(id=1)
        cls.backend = 'users.auth_backends.PhoneNumberBackend'
        cls.custom_client = Client.objects.get(id=1)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_redirect_anon_user_from_create_order_url(self):
        url = 'products:create-order'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 302)

    def test_product_detail_url(self):
        response = self.client.get(reverse('products:product-detail',
                                           kwargs={'slug': self.product.slug}))
        self.assertEqual(response.status_code, 200)

    def test_url_category(self):
        categories = ('pizza', 'burger', 'roll')
        for category in categories:
            with self.subTest(msg=f'Тест категории: {category}'):
                response = self.client.get(
                    reverse('products:product-list',
                            kwargs={'category': category}))
                self.assertEqual(response.status_code, 200)

    def test_invalid_category(self):
        response = self.client.get('products/invalid_category/')
        self.assertEqual(response.status_code, 404)

    def test_cart(self):
        data = [('products:cart', 'products/cart.html', 200),
                ('products:cart-clear', None, 302)]
        for url, template, status_code in data:
            with self.subTest(msg=f'Тест {url}'):
                response = self.client.get(reverse(url))
                self.assertEqual(response.status_code, status_code)
                if template is not None:
                    self.assertTemplateUsed(response, template)

    def test_cart_with_product_slug(self):
        data = [('products:add_to_cart', 302),
                ('products:increase-count', 302),
                ('products:decrease-count', 302)]
        for url, status_code in data:
            with self.subTest(msg=f'Тест {url}'):
                response = self.client.get(
                    reverse(url, kwargs={'slug': self.product.slug}))
                self.assertEqual(response.status_code, status_code)

    def test_order_url_for_auth_user(self):
        self.client.force_login(self.custom_client, backend=self.backend)
        response = self.client.get(reverse('products:create-order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/order_create.html')

    def test_order_url_for_anon_user(self):
        response = self.client.get(reverse('products:create-order'))
        self.assertEqual(response.status_code, 302)
