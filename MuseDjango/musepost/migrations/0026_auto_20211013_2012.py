# Generated by Django 3.2.7 on 2021-10-13 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("musepost", "0025_alter_post_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="최초 업로드 날짜",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="modified_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="최근 수정 날짜",
            ),
            preserve_default=False,
        ),
    ]
