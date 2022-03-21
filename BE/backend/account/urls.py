from django.urls import path
from account.views import (
    UserRegisterView,
    RefreshView,
    LogoutView
)

from rest_framework_simplejwt.views import TokenObtainPairView


app_name = "account"
urlpatterns = [
    path('', UserRegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout')
]