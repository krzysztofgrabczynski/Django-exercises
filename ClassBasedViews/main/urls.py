from django.urls import path
from .views import TimeTemplateView


urlpatterns = [
    path('template-view/', TimeTemplateView.as_view(), name='template-view')
]
