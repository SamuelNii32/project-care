# Generated by Django 4.1.1 on 2022-10-19 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0007_subscribe"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Subscribe",
            new_name="Subscriber",
        ),
        migrations.AlterModelOptions(
            name="subscriber",
            options={"verbose_name_plural": "Subscribers"},
        ),
    ]