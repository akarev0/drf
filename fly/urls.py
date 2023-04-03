from django.urls import path
from .views import (
    FlightListView,
    FlightDetailView,
    JetsListView,
    FlightDepartureListView,
)


app_name = "fly"

urlpatterns = [
    path("", FlightListView.as_view(), name="list"),
    path("<int:pk>/", FlightDetailView.as_view(), name="detail"),
    path("jets", JetsListView.as_view(), name="jets"),
    path("range", FlightDepartureListView.as_view(), name="range"),
]
