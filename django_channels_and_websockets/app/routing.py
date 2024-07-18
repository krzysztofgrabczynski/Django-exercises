from django.urls import re_path

from app.consumers import ChatConsumer


websocket_urlpatterns = [
    re_path(r"ws/websocket/", ChatConsumer.as_asgi()),
]
