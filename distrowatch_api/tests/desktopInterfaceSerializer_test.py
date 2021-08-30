from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from distrowatch_api.serializers import DesktopInterfaceSerializer

from .factories import DesktopInterfaceFactory


class DesktopInterfaceSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.desktopInterface = DesktopInterfaceFactory.create()

    def test_that_a_desktopInterface_is_correctly_serialized(self):
        desktopInterface = self.desktopInterface
        serializer = DesktopInterfaceSerializer
        serialized_desktopInterface = serializer(desktopInterface).data

        assert serialized_desktopInterface['id'] == desktopInterface.id
        assert serialized_desktopInterface['name'] == desktopInterface.name
