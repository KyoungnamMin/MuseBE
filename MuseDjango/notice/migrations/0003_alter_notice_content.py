# Generated by Django 3.2.7 on 2022-01-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_alter_notice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='내용'),
        ),
    ]
