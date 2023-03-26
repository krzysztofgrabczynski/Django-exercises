from django.urls import path
from main import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('create_obj/', views.create_obj, name='create_obj'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]