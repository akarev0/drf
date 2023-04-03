from rest_framework import serializers
from fly.models import Flight, Aircraft


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "departure_airport",
            "arrival_airport",
            "aircraft",
        )


class FlightDepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ("departure_airport",)


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ("id", "serial_number", "manufacturer")
