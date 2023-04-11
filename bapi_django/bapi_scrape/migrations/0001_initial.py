# Generated by Django 4.1.5 on 2023-02-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                ("category", models.CharField(max_length=30)),
                ("course_name", models.CharField(max_length=250)),
                ("instructor", models.CharField(max_length=100)),
                ("course_description", models.TextField()),
                ("enrolled", models.IntegerField()),
                ("ratings", models.IntegerField()),
            ],
        ),
    ]