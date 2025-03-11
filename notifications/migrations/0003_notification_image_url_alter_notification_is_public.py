# Generated by Django 4.2.6 on 2025-03-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "notifications",
            "0002_remove_notification_recipient_notification_user_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="notification",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
