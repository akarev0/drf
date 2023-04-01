from rest_framework import generics
from .serializers import FlightSerializer, AircraftSerializer
from fly.models import Flight, Aircraft
from django_filters.rest_framework import DjangoFilterBackend


class FlightListView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "arrival_airport",
        "departure_airport",
        "departure_time",
        "arrival_time",
    ]


class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


# jets


class JetsListView(generics.ListCreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
