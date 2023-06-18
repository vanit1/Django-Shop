from django.contrib import admin
from django.urls import path, include
from shop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/', include('cart.urls'), name='cart'),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls'), name='orders'),
    path('', include('Products.urls'), name='products'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

