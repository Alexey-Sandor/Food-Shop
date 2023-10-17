from django.test import TestCase
from django.urls import reverse

from products.models import Product


class ProductViewTestCase(TestCase):
    fixtures = ['product']

    def setUp(self):
        self.product = Product.objects.get(id=1)

    def test_empty_product_queryset(self):
        """
        Проверка, что QuerySet продуктов пустой для указанной категории.
        """
        response = self.client.get(reverse('products:product-list',
                                           kwargs={'category': 'pizza'}))
        self.assertEqual(len(response.context.get('products')), 0)

    def test_not_empty_product_queryset(self):
        """
        Проверка, что QuerySet продуктов возращает объекты данной категории.
        """
        response = self.client.get(reverse('products:product-list',
                                           kwargs={'category': 'roll'}))

        products = response.context.get('products')

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, 'Ролл Филадельфия')
