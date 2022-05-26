from django.urls import path

from .views import (
  NotificationWeeklyView,
)

app_name = "notification"
urlpatterns = [
    path('weekly/', NotificationWeeklyView.as_view(), name="notification_api"),
]