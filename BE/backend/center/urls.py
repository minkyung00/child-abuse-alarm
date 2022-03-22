from django.urls import path

from .views import (
  CenterView,
  CenterCodeView,
)

app_name = "center"
urlpatterns = [
    path('', CenterView.as_view(), name="center_api"),
    path('<int:center_id>/code/', CenterCodeView.as_view(), name="center_code_api"),
]