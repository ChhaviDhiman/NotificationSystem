from django.urls import path, include
from rest_framework import routers
from . import views
from .views import NotificationViewSet  # Make sure this is imported correctly

router = routers.DefaultRouter()
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
    path('public-notifications/', views.PublicNotificationListView.as_view(), name='public-notifications'),
    path('private-notifications/', views.PrivateNotificationListView.as_view(), name='private-notifications'),
]
