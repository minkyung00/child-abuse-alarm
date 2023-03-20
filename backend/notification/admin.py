from django.contrib import admin

from . import models

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'content',
        'created_time',
        'is_alert',
        'is_read',
        'target_center',
        'target_user'
    )

    list_display_links = (
        'target_center',
        'target_user'
    )
