# Generated by Django 5.0.6 on 2024-11-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climbed", "0002_rename_sport_type_workout_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workout",
            name="date",
            field=models.DateField(),
        ),
    ]
