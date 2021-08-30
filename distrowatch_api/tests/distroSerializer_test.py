from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from distrowatch_api.serializers import DistroSerializer

from .factories import DistroFactory


class DistroSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.distro = DistroFactory.create()

    def test_that_a_distro_is_correctly_serialized(self):
        distro = self.distro
        serializer = DistroSerializer
        serialized_distro = serializer(distro).data

        assert serialized_distro['id'] == distro.id
        assert serialized_distro['name'] == distro.name
        assert serialized_distro['description'] == distro.description
        assert serialized_distro['logo'] == distro.logo
        assert serialized_distro['price'] == distro.price
        assert serialized_distro['os_type'] == distro.os_type
        assert serialized_distro['origin'] == distro.origin
        assert serialized_distro['based_on'] == distro.based_on
        assert serialized_distro['category'] == distro.category
        assert serialized_distro['status'] == distro.status
        assert serialized_distro['popularity'] == distro.popularity
        assert serialized_distro['home_page'] == distro.home_page
        assert serialized_distro['user_forums'] == distro.user_forums
