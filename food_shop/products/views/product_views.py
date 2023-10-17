from django.views.generic import DetailView, ListView

from products.models import Product


class ProductListView(ListView):
    """
    Представление для отображения списка товаров определенной категории.

    Атрибуты:

    - model - модель Product
    - template_name - имя шаблона списка
    - context_object_name - имя списка в контексте шаблона

    Методы:

    - get_queryset() - фильтрует товары по категории и доступности.

    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['category'],
                                         available=True)


class ProductDelaitView(DetailView):
    """
    Представление для отображения детальной информации о товаре.

    Атрибуты:

    - model - модель Product
    - context_object_name - имя объекта товара в контексте
    - template_name - имя шаблона детальной страницы
    - queryset - запрос на получение товара по параметру slug

    Отображает детальную страницу выбранного товара.

    """
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
    queryset = model.objects.all()
