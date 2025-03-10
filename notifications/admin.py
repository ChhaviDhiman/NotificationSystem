from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'is_public', 'user', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'message', 'user__username')
