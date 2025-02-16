from django.urls import re_path
from .consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from django_channels_jwt_auth_middleware.auth import JWTAuthMiddlewareStack


websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>[\w-]+)/$", ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": JWTAuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})