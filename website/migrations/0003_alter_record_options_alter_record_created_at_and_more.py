# Generated by Django 4.2.3 on 2023-08-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_rename_records_record"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="record",
            options={"verbose_name": "Record", "verbose_name_plural": "Records"},
        ),
        migrations.AlterField(
            model_name="record",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]
