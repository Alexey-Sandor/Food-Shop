
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from products import views

app_name = 'products'

products_urls = [
    re_path(r'^products/(?P<category>(pizza|burger|roll))/$',
            views.ProductListView.as_view(), name='product-list'),
    path('product/<slug>/', views.ProductDelaitView.as_view(),
         name='product-detail'),
]

cart_urls = [
    path('cart', views.CartView.as_view(), name='cart'),
    path('add_to_cart/<slug>/', views.add_product_to_cart, name='add_to_cart'),
    path('increase_count/<slug>/', views.increase_product_amount,
         name='increase-count'),
    path('decrease_count/<slug>/', views.decrease_product_amount,
         name='decrease-count'),
    path('cart_clear/', views.clear_cart, name='cart-clear'),
]

order_urls = [
    path('order/', views.OrderView.as_view(), name='create-order'),
    path('order/success-created',
         TemplateView.as_view(
             template_name='products/order_success_created.html'),
         name='order-success-created'),
]
urlpatterns = [
    path('', TemplateView.as_view(template_name='products/home.html'),
         name='home'),
    path('', include(products_urls)),
    path('', include(cart_urls)),
    path('', include(order_urls))
]
