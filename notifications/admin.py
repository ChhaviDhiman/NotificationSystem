from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_public', 'read', 'read_at', 'created_at')
    list_filter = ('is_public', 'read')
    search_fields = ('title', 'message', 'user__username')
