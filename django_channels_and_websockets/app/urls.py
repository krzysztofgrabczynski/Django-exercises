from django.urls import path

from app import views

urlpatterns = [
    path("chat/", views.chat, name="chat"),
]
