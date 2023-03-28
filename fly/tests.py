from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestFly(APITestCase):
    def test_get_flights(self) -> None:
        url = reverse("fly:list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
