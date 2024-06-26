# Generated by Django 4.2.10 on 2024-03-18 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0004_remove_author_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="biological_info",
            field=models.TextField(default="No biological information available"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=models.TextField(default="No content available"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="comment",
            field=models.TextField(default="No comment available"),
        ),
    ]
