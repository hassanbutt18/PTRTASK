# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserRegistrationViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('registration', UserRegistrationViewSet, basename='user_registration')
router.register('', UserRegistrationViewSet, basename='user_registration')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
