# Generated by Django 3.2.7 on 2021-12-31 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musepost', '0042_auto_20211231_1402'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='MUSE_Post_Comments',
        ),
        migrations.AlterModelTable(
            name='post',
            table='MUSE_Post',
        ),
        migrations.AlterModelTable(
            name='postbookmark',
            table='MUSE_Post_Bookmark',
        ),
        migrations.AlterModelTable(
            name='postlike',
            table='MUSE_Post_Like',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='MUSE_Tag',
        ),
        migrations.AlterModelTable(
            name='taggedpost',
            table='MUSE_TaggedPost',
        ),
    ]