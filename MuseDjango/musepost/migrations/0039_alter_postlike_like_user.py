# Generated by Django 3.2.7 on 2021-12-28 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musepost', '0038_auto_20211228_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='like_user',
            field=models.ForeignKey(db_column='like_user', default='default', on_delete=django.db.models.deletion.CASCADE, related_name='likeUser', to=settings.AUTH_USER_MODEL, to_field='user_id', verbose_name='좋아요 누른 유저'),
        ),
    ]