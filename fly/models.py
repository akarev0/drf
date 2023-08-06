from django.db import models


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.manufacturer}-{self.serial_number}"


class Flight(models.Model):
    class Airport(models.TextChoices):
        SOLOMON_ISLANDS = "AG", "Solomon Islands"
        NAURU = "AN", "Nauru"
        PAPUA_NEW_GUINEA = "AY", "Papua New Guinea"
        GREENLAND = "BG", "Greenland"
        ICELAND = "BI", "Iceland"
        KOSOVO = "BK", "Kosovo"
        CANADA = "C", "Canada"
        ALGERIA = "DA", "Algeria"
        BENIN = "DB", "Benin"
        BURKINO_FASO = "DF", "Burkina Faso"
        GHANA = "DG", "Ghana"
        COTE_DVOIRE = "DI", "Côte d'Ivoire"
        NIGERIA = "DN", "Nigeria"
        NIFER = "DR", "Niger"
        TUNISIA = "DT", "Tunisia"
        TOGO = "DX", "Togo"
        BELGIUM = "EB", "Belgium"
        GERMANY = "ED", "Germany (civil)"
        ESTONIA = "EE", "Estonia"
        FINLAND = "EF", "Finland"
        UNITED_KINGDOM = "EG", "United Kingdom (and Crown Dependencies)"
        NETHERLANDS = "EH", "Netherlands"
        IRELAND = "EI", "Ireland"
        DENMARK = "EK", "Denmark and the Faroe Islands"
        LUXEMBOURG = "EL", "Luxembourg"
        CONGO = "FZ", "Democratic Republic of the Congo"

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    departure_airport = models.CharField(choices=Airport.choices, max_length=255)
    arrival_airport = models.CharField(choices=Airport.choices, max_length=255)
    # An aircraft, that can be assigned to the flight at its creation or later
    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.PROTECT, default=None, blank=True, null=True
    )
