# Generated by Django 3.2.7 on 2021-10-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211018_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
