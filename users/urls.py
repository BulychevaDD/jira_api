from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomObtainTokenPairView, RegisterView, UserInfoView

urlpatterns = [
    path('token', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterView.as_view(), name='user_register'),
    path('info', UserInfoView.as_view(), name='user_info'),
]
