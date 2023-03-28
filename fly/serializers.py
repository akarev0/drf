from rest_framework import serializers
from fly.models import Flight, Aircraft


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrivalat_time",
            "departure_airport",
            "arrival_airport",
            "aicraft",
        )

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = (
            "id",
            "serial_number",
            "manufacturer"
        )