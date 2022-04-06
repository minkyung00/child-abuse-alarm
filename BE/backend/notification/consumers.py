from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification

# Notification 모델에 데이터가 추가되면 -> 이 정보를 NotificationConsumer에 있는 share_message에 보냄 -> 정보를 웹소켓이 연결된 페이지로 전송

@receiver(post_save, sender=Notification)
def announce_likes(sender, instance, created, **kwargs):
    if created:
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "shares", {
                "type": "share_message",
                "message": instance.message,
            }
    )
# @database_sync_to_async
# def get_user(user_id):
#     try:
#         return Users.objects.get(id=user_id)
#     except:
#         return AnonymousUser()


# @database_sync_to_async
# def create_notification(receiver,typeof="task_created",status="unread"):
#     notification_to_create=notifications.objects.create(user_revoker=receiver,type_of_notification=typeof)
#     print('I am here to help')
#     return (notification_to_create.user_revoker.username,notification_to_create.type_of_notification)


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.center_name = self.scope['url_route']['kwargs']['center_name'] # notification/routing.py에 있는 center_name 
        self.accept() # websocket 연결 
        
        async_to_sync(self.channel_layer.group_add)( # group 참여
            self.center_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.center_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to group
        async_to_sync(self.channel_layer.group_send)(
            self.center_name,
            {
                'type': 'share_message',
                'message': message
            }
        )

    # Receive message from room group
    def share_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))