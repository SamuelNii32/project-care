# Generated by Django 4.1.1 on 2022-10-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0011_transaction_phone_alter_transaction_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="occurred",
            field=models.DateTimeField(auto_now=True, help_text="Date of transaction"),
        ),
    ]
