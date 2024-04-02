# Generated by Django 4.2.10 on 2024-03-19 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_rename_authors_author_alter_comment_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogs",
                to="blog.author",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.blogpost",
            ),
        ),
    ]
