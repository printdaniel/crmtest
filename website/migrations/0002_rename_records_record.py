# Generated by Django 4.2.3 on 2023-08-02 18:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Records",
            new_name="Record",
        ),
    ]
