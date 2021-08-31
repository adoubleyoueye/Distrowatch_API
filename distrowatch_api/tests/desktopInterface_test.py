import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import DesktopInterface
from .factories import DesktopInterfaceFactory, DistroFactory

faker = Factory.create()


class DesktopInterface_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        DesktopInterfaceFactory.create_batch(size=3)

    def test_get_one(self):
        client = self.api_client
        desktopInterface_pk = DesktopInterface.objects.first().pk
        desktopInterface_detail_url = reverse(
            'desktop_interface-detail', kwargs={'pk': desktopInterface_pk})
        response = client.get(desktopInterface_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('desktop_interface-list'))
        assert response.status_code == status.HTTP_200_OK
        assert DesktopInterface.objects.count() == len(response.data)
