"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

# from django.core.asgi import get_asgi_application
import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

import notification.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# 서버로 연결이 생성되면 먼저 ProtocolTypeRouter가 연결의 종류를 탐색
# ws:// 혹은 wss:// 형식의 웹 소켓 연결이면, 해당 연결은 AuthMiddlewareStack으로 메시지를 group의 모든 channel에게 보낸다
application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            notification.routing.websocket_urlpatterns
        )
    ),
})

# application = get_asgi_application()
