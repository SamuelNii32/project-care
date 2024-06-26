# Generated by Django 4.1.1 on 2022-09-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_alter_department_options_remove_topic_abstract_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="brief",
            field=models.TextField(
                blank=True,
                default=None,
                help_text="Project Abstract",
                max_length=10000,
                null=True,
            ),
        ),
    ]
