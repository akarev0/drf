# Generated by Django 4.1.7 on 2023-03-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fly", "0003_alter_flight_arrival_airport_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircraft",
            name="serial_number",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
