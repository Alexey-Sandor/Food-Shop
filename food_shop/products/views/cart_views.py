from django.shortcuts import redirect, render
from django.views import View

from products.cart import Cart
from products.models import Product


class CartView(View):
    """
    Вьюха для отображения корзины пользователя.
    """
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'products/cart.html',
                      {'cart': cart.get_products()})


def add_product_to_cart(request, slug):
    """
    Вьюха для добавления товара в корзину
    """
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.add_product_to_cart(product.slug, product.name, product.price,
                             product.weight, product.image)
    return redirect('products:product-list', category=product.category)


def increase_product_amount(request, slug):
    """
    Вьюха для увеличения количества продукта в корзине
    """
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.increase_product_amount(slug, product.price)
    return redirect('products:cart')


def decrease_product_amount(request, slug):
    """
    Вьюха для уменьшения количества продукта в корзине
    """
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.decrease_product_amount(slug, product.price)
    return redirect('products:cart')


def clear_cart(request):
    """
    Вьюха для учистки корзины
    """
    cart = Cart(request)
    cart.clear()
    return redirect('products:cart')
