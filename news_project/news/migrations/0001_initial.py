# Generated by Django 5.0.6 on 2024-06-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Favorite",
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
                ("title", models.CharField(max_length=512)),
                ("description", models.TextField()),
                ("url", models.URLField()),
                ("published_at", models.DateTimeField()),
                ("author", models.CharField(max_length=128)),
            ],
        ),
    ]
