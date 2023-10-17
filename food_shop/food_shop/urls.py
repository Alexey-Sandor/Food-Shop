
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path


# временное решение проблемы отрисовки
# шаблона 404 из коробки
def handler404(request, exception):
    return render(request, '404/404.html', status=404)


handler404 = handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('products.urls')),

]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
