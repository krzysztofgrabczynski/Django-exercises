from django.contrib import admin
from django.urls import path, include

from payment import urls as payment_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include(payment_urls)),
]
