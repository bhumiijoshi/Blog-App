# Generated by Django 4.2.10 on 2024-03-19 06:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0009_authors_comment_remove_author_user_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Authors",
            new_name="Author",
        ),
        migrations.AlterModelTable(
            name="comment",
            table="comments",
        ),
    ]
