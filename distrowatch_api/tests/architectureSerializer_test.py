from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from distrowatch_api.serializers import ArchitectureSerializer

from .factories import ArchitectureFactory


class ArchitectureSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.architecture = ArchitectureFactory.create()

    def test_that_a_architecture_is_correctly_serialized(self):
        architecture = self.architecture
        serializer = ArchitectureSerializer
        serialized_architecture = serializer(architecture).data

        assert serialized_architecture['id'] == architecture.id
        assert serialized_architecture['name'] == architecture.name
