from django.urls import path
from .views import ProductView

urlpatterns = [
    path('index/', ProductView.as_view(), name='index'),
]