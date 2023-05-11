from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat import consumers

http_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": http_application,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/chat/", consumers.ChatConsumer.as_asgi()),
                ]
            )
        ),
    }
)
