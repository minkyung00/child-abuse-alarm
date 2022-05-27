from django.urls import re_path
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notification/(?P<center_name>\w+)/$', consumers.NotificationConsumer.as_asgi()),
    # url(r'^ws/notification/(?P<center_name>[^/]+)/$', consumers.NotificationConsumer)
]