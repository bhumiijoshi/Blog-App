# Generated by Django 4.2.10 on 2024-03-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_comment_comment_post_date_author_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="biological_info",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
