from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import SignUpView, CurrentUserView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('me/', CurrentUserView.as_view(), name='current_user'),
]
