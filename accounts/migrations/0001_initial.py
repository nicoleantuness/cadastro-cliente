# Generated by Django 4.1.3 on 2023-02-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
                ("telephone", models.IntegerField()),
                ("date_register", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]