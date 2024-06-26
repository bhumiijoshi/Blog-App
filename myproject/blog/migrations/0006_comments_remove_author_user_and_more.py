# Generated by Django 4.2.10 on 2024-03-18 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_author_user_alter_author_biological_info_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("comment", models.TextField()),
            ],
            options={
                "db_table": "comments",
            },
        ),
        migrations.RemoveField(
            model_name="author",
            name="user",
        ),
        migrations.AlterField(
            model_name="author",
            name="biological_info",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.AddField(
            model_name="comments",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.blogpost"
            ),
        ),
    ]
