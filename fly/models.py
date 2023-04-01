from typing import Collection, Optional
from django.db import models
from django.forms import ValidationError

options = [
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
]


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.manufacturer}-{self.serial_number}"


class Flight(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    departure_airport = models.CharField(choices=options, max_length=255)
    arrival_airport = models.CharField(choices=options, max_length=255)
    # An aircraft, that can be assigned to the flight at its creation or later
    aicraft = models.ForeignKey(
        Aircraft, on_delete=models.PROTECT, default=None, blank=True, null=True
    )
