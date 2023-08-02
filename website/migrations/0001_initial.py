# Generated by Django 4.2.3 on 2023-08-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Records",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("zipcode", models.CharField(max_length=20)),
            ],
        ),
    ]
