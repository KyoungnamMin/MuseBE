# Generated by Django 3.2.7 on 2021-12-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20211117_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instar_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='인스타 ID'),
        ),
    ]
