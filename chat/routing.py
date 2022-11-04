from django.urls import path

from . import consumers

websocket_urlpatterns = [
    # path(r'chat/', consumers.ChatConsumer.as_asgi()),
    path('chat/', consumers.PublicGroupConsumer.as_asgi()),
]