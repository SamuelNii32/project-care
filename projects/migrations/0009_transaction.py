# Generated by Django 4.1.1 on 2022-10-16 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_alter_topic_brief"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        default=None, help_text="First Name", max_length=60
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        default=None, help_text="Last Name", max_length=60
                    ),
                ),
                ("email", models.EmailField(help_text="Email", max_length=254)),
                (
                    "paid",
                    models.CharField(
                        default="0.00", help_text="Amount Paid", max_length=60
                    ),
                ),
                (
                    "reference",
                    models.CharField(
                        default="", help_text="Transaction Reference", max_length=255
                    ),
                ),
                (
                    "files_sent",
                    models.BooleanField(default=False, help_text="Files Sent"),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        help_text="Project Topic",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="projects.topic",
                    ),
                ),
            ],
        ),
    ]
