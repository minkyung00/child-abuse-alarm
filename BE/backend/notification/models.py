from django.db import models

from account.models import User

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    created_time = models.DateTimeField(auto_now_add=True)
    is_alert = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="username", to_field="username")

    class Meta:
        db_table = "notification"