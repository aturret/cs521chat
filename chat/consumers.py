import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message

# class ChatConsumer(AsyncWebsocketConsumer):
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = text_data_json['user']
        message = text_data_json['message']

        # Store the message in the database
        await self.save_message(user, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': user,
                'message': message,
            }
        )

    async def chat_message(self, event):
        user = event['user']
        message = event['message']

        await self.send(text_data=json.dumps({
            'user': user,
            'message': message,
        }))

    # Add this method to store messages in the database
    @database_sync_to_async
    def save_message(self, user, content):
        message = Message(user=user, content=content)
        message.save()

    # async def connect(self):
    #     await self.accept()
    #
    # async def disconnect(self, close_code):
    #     pass
    #
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     user = text_data_json['user']
    #
    #     await self.send(text_data=json.dumps({'user': user, 'message': message}))
