import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Architecture
from .factories import ArchitectureFactory, DistroFactory

faker = Factory.create()


class Architecture_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        ArchitectureFactory.create_batch(size=3)

    def test_get_one(self):
        client = self.api_client
        architecture_pk = Architecture.objects.first().pk
        architecture_detail_url = reverse('architecture-detail', kwargs={'pk': architecture_pk})
        response = client.get(architecture_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('architecture-list'))
        assert response.status_code == status.HTTP_200_OK
        assert Architecture.objects.count() == len(response.data)
