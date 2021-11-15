# Generated by Django 3.2.7 on 2021-10-12 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("musepost", "0021_auto_20211011_1838"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="comment_writer",
            new_name="writer",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="body_text",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="tags",
            new_name="hashtag",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="body_image",
            new_name="image",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="liked",
            new_name="likes",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="hits",
            new_name="views",
        ),
    ]
