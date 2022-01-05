# Generated by Django 3.2.7 on 2022-01-06 03:35

import accounts.models
import common.upload_file
import config.asset_storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100, unique=True, verbose_name='아이디')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=100, verbose_name='이름')),
                ('nickname', models.CharField(max_length=50, unique=True, verbose_name='닉네임')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='최초 가입 날짜')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='최근 로그인 날짜')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '유저',
                'db_table': 'MUSE_User',
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='accounts.user', to_field='user_id', verbose_name='유저')),
                ('badge', models.IntegerField(default=0, verbose_name='뱃지 개수')),
                ('rep_badge', models.ImageField(blank=True, null=True, storage=config.asset_storage.PublicMediaStorage(), upload_to=common.upload_file.upload_post_image, verbose_name='대표 뱃지')),
                ('avatar', models.ImageField(blank=True, null=True, storage=config.asset_storage.PublicMediaStorage(), upload_to=common.upload_file.upload_profile_image, verbose_name='프로필 사진')),
                ('self_introduce', models.CharField(blank=True, max_length=100, null=True, verbose_name='자기 소개')),
                ('instar_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='인스타 ID')),
            ],
            options={
                'verbose_name_plural': '유저 프로필',
                'db_table': 'MUSE_UserProfile',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, to_field='user_id', verbose_name='팔로우 눌린 사람')),
                ('following', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, to_field='user_id', verbose_name='팔로우 누른 사람')),
            ],
            options={
                'verbose_name_plural': '팔로우',
                'db_table': 'MUSE_UserFollow',
            },
        ),
    ]
