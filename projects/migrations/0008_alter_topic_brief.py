# Generated by Django 4.1.1 on 2022-10-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_rename_extention_topic_extension"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="brief",
            field=models.TextField(
                blank=True, help_text="Project Brief", max_length=100000, null=True
            ),
        ),
    ]
