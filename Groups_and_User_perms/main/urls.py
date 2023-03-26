from django.urls import path
from main import views


urlpatterns = [
    path('index/', views.index, name='index'),

    path('create_film/', views.create_film, name='create_film'),
    path('create_book/', views.create_book, name='create_book'),
    path('create_article/', views.create_article, name='create_article'),
    
]