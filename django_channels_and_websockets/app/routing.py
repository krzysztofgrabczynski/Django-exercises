from django.urls import re_path

from app.consumers import ChatConsumer, ImageDownloadConsumer


websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    re_path(r"ws/notification/(?P<client_uuid>[0-9a-f-]{36})/$", ImageDownloadConsumer.as_asgi()),
]
