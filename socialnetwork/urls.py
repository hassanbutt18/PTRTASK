# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from socialnetwork.views import PostViewSet

router = DefaultRouter()
router.register('create', PostViewSet, basename='user_registration')
router.register('', PostViewSet, basename='user_registration')

urlpatterns = [
    path('api/', include(router.urls)),
]
