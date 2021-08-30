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

    def test_create_architecture(self):
        """
        Ensure we can create a new architecture object.
        """
        client = self.api_client
        architecture_count = Architecture.objects.count()
        architecture_dict = factory.build(dict, FACTORY_CLASS=ArchitectureFactory)
        response = client.post(reverse('architecture-list'), architecture_dict)
        created_architecture_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert Architecture.objects.count() == architecture_count + 1
        architecture = Architecture.objects.get(pk=created_architecture_pk)

        assert architecture_dict['name'] == architecture.name

    def test_create_architecture_with_m2m_relations(self):
        client = self.api_client

        distros = DistroFactory.create_batch(size=3)
        distros_pks = [distro.pk for distro in distros]

        architecture_dict = factory.build(
            dict, FACTORY_CLASS=ArchitectureFactory, distros=distros_pks)

        response = client.post(reverse('architecture-list'), architecture_dict)
        created_architecture_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED

        architecture = Architecture.objects.get(pk=created_architecture_pk)
        assert distros[0].architectures.first().pk == architecture.pk
        assert architecture.distros.count() == len(distros)

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

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        architecture_qs = Architecture.objects.all()
        architecture_count = Architecture.objects.count()

        for i, architecture in enumerate(architecture_qs, start=1):
            response = client.delete(reverse('architecture-detail', kwargs={'pk': architecture.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert architecture_count - i == Architecture.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        architecture_pk = Architecture.objects.first().pk
        architecture_detail_url = reverse('architecture-detail', kwargs={'pk': architecture_pk})
        architecture_dict = factory.build(dict, FACTORY_CLASS=ArchitectureFactory)
        response = client.patch(architecture_detail_url, data=architecture_dict)
        assert response.status_code == status.HTTP_200_OK

        assert architecture_dict['name'] == response.data['name']

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        architecture = Architecture.objects.first()
        architecture_detail_url = reverse('architecture-detail', kwargs={'pk': architecture.pk})
        architecture_name = architecture.name
        data = {
            'name': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(architecture_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert architecture_name == Architecture.objects.first().name
