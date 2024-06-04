# Generated by Django 4.1.1 on 2022-10-17 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Title",
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
                    "name",
                    models.CharField(help_text="Title of question", max_length=155),
                ),
            ],
            options={
                "verbose_name_plural": "Titles",
            },
        ),
        migrations.CreateModel(
            name="Asked",
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
                ("question", models.CharField(help_text="Question", max_length=255)),
                ("answer", models.TextField(help_text="Answer", max_length=50000)),
                ("posted", models.DateField(auto_now=True)),
                (
                    "title",
                    models.ForeignKey(
                        help_text="Title of question",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="faqs.title",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Asked",
            },
        ),
    ]
