# Generated by Django 3.2.7 on 2021-10-11 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("musepost", "0018_auto_20211011_1802"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment_writer",
            field=models.ForeignKey(
                blank=True,
                db_column="comment_writer",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="commentWriter",
                to=settings.AUTH_USER_MODEL,
                to_field="nickname",
            ),
        ),
        migrations.AlterField(
            model_name="postlike",
            name="like_user",
            field=models.ForeignKey(
                blank=True,
                db_column="like_user",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="likeUser",
                to=settings.AUTH_USER_MODEL,
                to_field="nickname",
            ),
        ),
    ]
