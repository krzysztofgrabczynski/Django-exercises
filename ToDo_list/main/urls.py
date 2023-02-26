from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('undo/', views.undo, name='undo'),
    path('redo/', views.redo, name='redo'),
    path('save/', views.save, name='save'),
]
