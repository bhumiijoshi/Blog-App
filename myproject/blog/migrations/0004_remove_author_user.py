# Generated by Django 4.2.10 on 2024-03-18 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_author_biological_info_alter_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]
