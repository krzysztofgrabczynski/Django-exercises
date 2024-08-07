import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "chat_message",
                "message": message,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))


class ImageDownloadConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope["url_route"]["kwargs"]["client_uuid"]
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_notification(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            'message': message 
        }))
