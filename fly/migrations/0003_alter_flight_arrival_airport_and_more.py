# Generated by Django 4.1.7 on 2023-03-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fly", "0002_alter_flight_aicraft"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="arrival_airport",
            field=models.CharField(
                choices=[
                    ("AG", "Solomon Islands"),
                    ("AN", "Nauru"),
                    ("AY", "Papua New Guinea"),
                    ("BG", "Greenland"),
                    ("BI", "Iceland"),
                    ("BK", "Kosovo"),
                    ("C", "Canada"),
                    ("DA", "Algeria"),
                    ("DB", "Benin"),
                    ("DF", "Burkina Faso"),
                    ("DG", "Ghana"),
                    ("DI", "Côte d'Ivoire"),
                    ("DN", "Nigeria"),
                    ("DR", "Niger"),
                    ("DT", "Tunisia"),
                    ("DX", "Togo"),
                    ("EB", "Belgium"),
                    ("ED", "Germany (civil)"),
                    ("EE", "Estonia"),
                    ("EF", "Finland"),
                    ("EG", "United Kingdom (and Crown Dependencies)"),
                    ("EH", "Netherlands"),
                    ("EI", "Ireland"),
                    ("EK", "Denmark and the Faroe Islands"),
                    ("EL", "Luxembourg"),
                    ("FZ", "Democratic Republic of the Congo"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="departure_airport",
            field=models.CharField(
                choices=[
                    ("AG", "Solomon Islands"),
                    ("AN", "Nauru"),
                    ("AY", "Papua New Guinea"),
                    ("BG", "Greenland"),
                    ("BI", "Iceland"),
                    ("BK", "Kosovo"),
                    ("C", "Canada"),
                    ("DA", "Algeria"),
                    ("DB", "Benin"),
                    ("DF", "Burkina Faso"),
                    ("DG", "Ghana"),
                    ("DI", "Côte d'Ivoire"),
                    ("DN", "Nigeria"),
                    ("DR", "Niger"),
                    ("DT", "Tunisia"),
                    ("DX", "Togo"),
                    ("EB", "Belgium"),
                    ("ED", "Germany (civil)"),
                    ("EE", "Estonia"),
                    ("EF", "Finland"),
                    ("EG", "United Kingdom (and Crown Dependencies)"),
                    ("EH", "Netherlands"),
                    ("EI", "Ireland"),
                    ("EK", "Denmark and the Faroe Islands"),
                    ("EL", "Luxembourg"),
                    ("FZ", "Democratic Republic of the Congo"),
                ],
                max_length=255,
            ),
        ),
    ]