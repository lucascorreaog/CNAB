# Generated by Django 4.1.2 on 2022-10-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
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
                ("transaction_type", models.CharField(max_length=255)),
                ("date", models.CharField(max_length=255)),
                ("amount", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=255)),
                ("card_number", models.CharField(max_length=255)),
                ("time", models.CharField(max_length=255)),
                ("store_owner", models.CharField(max_length=255)),
                ("store", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="FileUploader",
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
                ("upload", models.FileField(upload_to="upFiles/")),
            ],
        ),
    ]
