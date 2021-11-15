# Generated by Django 3.2.7 on 2021-10-10 07:51

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("musepost", "0007_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
