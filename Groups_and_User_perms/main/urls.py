from django.urls import path
from main import views


urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('index/', views.index, name='index'),
    path('create_obj/', views.create_obj, name='create_obj'),
    path('edit/<uuid:id>', views.edit, name='edit'),
    path('delete/<uuid:id>/', views.delete, name='delete'),
]