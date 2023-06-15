# Generated by Django 4.1.9 on 2023-06-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
            ],
        ),
        migrations.CreateModel(
            name="treasure",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("treasure_name", models.CharField(max_length=200)),
                ("treasure_description", models.CharField(max_length=200)),
                ("longitude", models.FloatField()),
                ("latitude", models.FloatField()),
                ("hint", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
    ]
