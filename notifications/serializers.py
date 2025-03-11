from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'title', 'message', 'is_public', 'image_url', 'created_at', 'read','read_at']
        read_only_fields = ['created_at', 'read_at']
