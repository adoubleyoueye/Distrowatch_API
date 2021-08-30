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

    def test_create_desktopInterface(self):
        """
        Ensure we can create a new desktopInterface object.
        """
        client = self.api_client
        desktopInterface_count = DesktopInterface.objects.count()
        desktopInterface_dict = factory.build(dict, FACTORY_CLASS=DesktopInterfaceFactory)
        response = client.post(reverse('desktop_interface-list'), desktopInterface_dict)
        created_desktopInterface_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert DesktopInterface.objects.count() == desktopInterface_count + 1
        desktopInterface = DesktopInterface.objects.get(pk=created_desktopInterface_pk)

        assert desktopInterface_dict['name'] == desktopInterface.name

    def test_create_desktopInterface_with_m2m_relations(self):
        client = self.api_client

        distros = DistroFactory.create_batch(size=3)
        distros_pks = [distro.pk for distro in distros]

        desktopInterface_dict = factory.build(
            dict, FACTORY_CLASS=DesktopInterfaceFactory, distros=distros_pks)

        response = client.post(reverse('desktop_interface-list'), desktopInterface_dict)
        created_desktopInterface_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED

        desktopInterface = DesktopInterface.objects.get(pk=created_desktopInterface_pk)
        assert distros[0].desktop_interfaces.first().pk == desktopInterface.pk
        assert desktopInterface.distros.count() == len(distros)

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

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        desktopInterface_qs = DesktopInterface.objects.all()
        desktopInterface_count = DesktopInterface.objects.count()

        for i, desktopInterface in enumerate(desktopInterface_qs, start=1):
            response = client.delete(reverse('desktop_interface-detail',
                                     kwargs={'pk': desktopInterface.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert desktopInterface_count - i == DesktopInterface.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        desktopInterface_pk = DesktopInterface.objects.first().pk
        desktopInterface_detail_url = reverse(
            'desktop_interface-detail', kwargs={'pk': desktopInterface_pk})
        desktopInterface_dict = factory.build(dict, FACTORY_CLASS=DesktopInterfaceFactory)
        response = client.patch(desktopInterface_detail_url, data=desktopInterface_dict)
        assert response.status_code == status.HTTP_200_OK

        assert desktopInterface_dict['name'] == response.data['name']

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        desktopInterface = DesktopInterface.objects.first()
        desktopInterface_detail_url = reverse(
            'desktop_interface-detail', kwargs={'pk': desktopInterface.pk})
        desktopInterface_name = desktopInterface.name
        data = {
            'name': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(desktopInterface_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert desktopInterface_name == DesktopInterface.objects.first().name
