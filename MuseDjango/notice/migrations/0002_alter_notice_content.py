# Generated by Django 3.2.7 on 2022-01-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='내용'),
        ),
    ]