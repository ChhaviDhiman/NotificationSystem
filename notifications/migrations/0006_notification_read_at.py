# Generated by Django 4.2.6 on 2025-03-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0005_alter_notification_is_public_alter_notification_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="read_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
