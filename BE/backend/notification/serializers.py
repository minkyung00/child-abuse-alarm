from rest_framework import serializers

from .models import Notification, NotificationWeekly

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'content', 'hit_count', 'kick_count', 'created_time', 'is_danger', 'is_warning', 'is_caution']

class NotificationWeeklySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationWeekly
        fields = '__all__'