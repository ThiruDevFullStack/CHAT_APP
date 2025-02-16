import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.contrib.auth.models import User

active_users = set()  # Store active users in a set

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]  # Get the authenticated user
        self.username = self.user.username if self.user.is_authenticated else None

        if self.user.is_authenticated:
            active_users.add(self.username)  # Add the user to the active list
            await self.channel_layer.group_add("active_users", self.channel_name)
            await self.broadcast_active_users()

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"✅ WebSocket Connected: {self.room_group_name}")


    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            active_users.discard(self.username)  # Remove user from active list
            await self.channel_layer.group_discard("active_users", self.channel_name)
            await self.broadcast_active_users()

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print(f"⚠️ WebSocket Disconnected: {self.room_group_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")
        username = data.get("username", "")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "type": "chat_message",
            "message": event["message"],
            "username": event["username"]
        }))

    async def broadcast_active_users(self):
        """Broadcast the list of active users to all connected clients."""
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            "active_users",
            {
                "type": "send_active_users",
                "users": list(active_users)
            }
        )

    async def send_active_users(self, event):
        """Send active users list to the frontend."""
        await self.send(text_data=json.dumps({
            "type": "active_users",
            "users": event["users"]
        }))
