from rest_framework import generics
from .serializers import FlightSerializer, AircraftSerializer, FlightDepartureSerializer
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


class FlightDepartureListView(generics.ListCreateAPIView):
    serializer_class = FlightDepartureSerializer

    def get_queryset(self):
        departure_time = self.request.query_params.get("departure_time")
        arrival_time = self.request.query_params.get("arrival_time")
        if not all([departure_time, arrival_time]):
            raise ValueError()

        return Flight.objects.filter(
            departure_time__gte=departure_time, arrival_time__lte=arrival_time
        )


# jets


class JetsListView(generics.ListCreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
