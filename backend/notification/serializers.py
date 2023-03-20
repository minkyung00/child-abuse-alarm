from rest_framework import serializers

from .models import Notification, NotificationWeekly

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'content', 'hit_count', 'kick_count', 'created_time', 'status']

class NotificationWeeklySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationWeekly
        fields = '__all__'