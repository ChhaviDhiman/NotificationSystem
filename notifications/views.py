from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from django.utils import timezone

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        read_status = request.data.get('read', None)
        
        if read_status is not None:
            instance.read = read_status
            if read_status:  # If the notification is marked as read
                instance.read_at = timezone.now()  # Record the time when it was read
            else:
                instance.read_at = None  # Reset if marked as unread
            instance.save()
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PublicNotificationListView(generics.ListAPIView):
    queryset = Notification.objects.filter(is_public=True)
    serializer_class = NotificationSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible

class PrivateNotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, is_public=False)
