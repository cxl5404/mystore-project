
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name="producthunt"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('cart/', include(('cart.urls'), namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^', include('shop.urls', namespace='shop')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
