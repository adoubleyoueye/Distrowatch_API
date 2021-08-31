import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Distro
from .factories import (
    ArchitectureFactory,
    DesktopInterfaceFactory,
    DistroFactory,
)

faker = Factory.create()


class Distro_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        DistroFactory.create_batch(size=3)

    def test_get_one(self):
        client = self.api_client
        distro_pk = Distro.objects.first().pk
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro_pk})
        response = client.get(distro_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('distro-list'))
        assert response.status_code == status.HTTP_200_OK
        assert Distro.objects.count() == len(response.data)
