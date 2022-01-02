# Generated by Django 3.2.7 on 2022-01-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musepost', '0045_auto_20211231_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('contest', '콘테스트'), ('reference', '레퍼런스')], max_length=30, null=True, verbose_name='게시물 카테고리'),
        ),
    ]