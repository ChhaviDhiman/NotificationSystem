from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Private if user is set
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_public = models.BooleanField(default=False)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)  # New field for tracking when the message was read
    
    class Meta:
        db_table = 'cargpt_notifications'

    def __str__(self):
        return self.title
