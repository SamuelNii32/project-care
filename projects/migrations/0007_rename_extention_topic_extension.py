# Generated by Django 4.1.1 on 2022-10-12 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_topic_extention_alter_topic_brief"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topic",
            old_name="extention",
            new_name="extension",
        ),
    ]
