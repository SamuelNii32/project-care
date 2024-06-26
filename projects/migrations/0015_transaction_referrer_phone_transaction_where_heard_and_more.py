# Generated by Django 4.1.2 on 2023-01-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0014_paystack"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="referrer_phone",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Referrer phone number",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="where_heard",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Where the person heard about Project Care",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="phone",
            field=models.CharField(
                default=None, help_text="Phone number", max_length=255
            ),
        ),
    ]
