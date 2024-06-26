# Generated by Django 4.2.10 on 2024-03-18 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="comment_post_date",
        ),
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="author",
            name="biological_info",
            field=models.TextField(default="", blank=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(default="", max_length=50, blank=True),
        ),
        migrations.AlterModelTable(
            name="comment",
            table="comment",
        ),
    ]
