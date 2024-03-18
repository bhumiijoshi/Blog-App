# Generated by Django 4.2.10 on 2024-03-18 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_comments_remove_author_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='author',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
