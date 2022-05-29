from django.db import models

from center.models import Center
from account.models import User

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    hit_count = models.IntegerField(default=0)
    kick_count = models.IntegerField(default=0)
    target_center = models.ForeignKey(Center, on_delete=models.CASCADE, db_column="target_center", null=True)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="username", to_field="username", null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True)
    is_alert = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "notification"

class NotificationWeekly(models.Model):
    start_date = models.DateTimeField()
    total_hit = models.IntegerField(default=0)
    total_kick = models.IntegerField(default=0)
    total_danger = models.IntegerField(default=0)
    total_warning = models.IntegerField(default=0)
    total_caution = models.IntegerField(default=0)

    class Meta:
        db_table = "notificationWeekly"