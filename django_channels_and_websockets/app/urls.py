from django.urls import path

from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("download_image/", views.download_image, name="download-image"),
    path("<str:room_name>/", views.chat, name="room"),
]
