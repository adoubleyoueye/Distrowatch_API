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

    def test_create_distro(self):
        """
        Ensure we can create a new distro object.
        """
        client = self.api_client
        distro_count = Distro.objects.count()
        distro_dict = factory.build(dict, FACTORY_CLASS=DistroFactory)
        response = client.post(reverse('distro-list'), distro_dict)
        created_distro_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert Distro.objects.count() == distro_count + 1
        distro = Distro.objects.get(pk=created_distro_pk)

        assert distro_dict['name'] == distro.name
        assert distro_dict['description'] == distro.description
        assert distro_dict['logo'] == distro.logo
        assert distro_dict['price'] == distro.price
        assert distro_dict['os_type'] == distro.os_type
        assert distro_dict['origin'] == distro.origin
        assert distro_dict['based_on'] == distro.based_on
        assert distro_dict['category'] == distro.category
        assert distro_dict['status'] == distro.status
        assert distro_dict['popularity'] == distro.popularity
        assert distro_dict['home_page'] == distro.home_page
        assert distro_dict['user_forums'] == distro.user_forums

    def test_create_distro_with_m2m_relations(self):
        client = self.api_client

        desktop_interfaces = DesktopInterfaceFactory.create_batch(size=3)
        desktop_interfaces_pks = [desktopInterface.pk for desktopInterface in desktop_interfaces]

        architectures = ArchitectureFactory.create_batch(size=3)
        architectures_pks = [architecture.pk for architecture in architectures]

        distro_dict = factory.build(dict, FACTORY_CLASS=DistroFactory,
                                    desktop_interfaces=desktop_interfaces_pks, architectures=architectures_pks)

        response = client.post(reverse('distro-list'), distro_dict)
        created_distro_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED

        distro = Distro.objects.get(pk=created_distro_pk)
        assert desktop_interfaces[0].distros.first().pk == distro.pk
        assert distro.desktop_interfaces.count() == len(desktop_interfaces)
        assert architectures[0].distros.first().pk == distro.pk
        assert distro.architectures.count() == len(architectures)

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

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        distro_qs = Distro.objects.all()
        distro_count = Distro.objects.count()

        for i, distro in enumerate(distro_qs, start=1):
            response = client.delete(reverse('distro-detail', kwargs={'pk': distro.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert distro_count - i == Distro.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        distro_pk = Distro.objects.first().pk
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro_pk})
        distro_dict = factory.build(dict, FACTORY_CLASS=DistroFactory)
        response = client.patch(distro_detail_url, data=distro_dict)
        assert response.status_code == status.HTTP_200_OK

        assert distro_dict['name'] == response.data['name']
        assert distro_dict['description'] == response.data['description']
        assert distro_dict['logo'] == response.data['logo']
        assert distro_dict['price'] == response.data['price']
        assert distro_dict['os_type'] == response.data['os_type']
        assert distro_dict['origin'] == response.data['origin']
        assert distro_dict['based_on'] == response.data['based_on']
        assert distro_dict['category'] == response.data['category']
        assert distro_dict['status'] == response.data['status']
        assert distro_dict['popularity'] == response.data['popularity']
        assert distro_dict['home_page'] == response.data['home_page']
        assert distro_dict['user_forums'] == response.data['user_forums']

    def test_update_price_with_incorrect_value_data_type(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_price = distro.price
        data = {
            'price': faker.pystr(),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_price == Distro.objects.first().price

    def test_update_popularity_with_incorrect_value_data_type(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_popularity = distro.popularity
        data = {
            'popularity': faker.pystr(),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_popularity == Distro.objects.first().popularity

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_name = distro.name
        data = {
            'name': faker.pystr(min_chars=33, max_chars=33),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_name == Distro.objects.first().name

    def test_update_description_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_description = distro.description
        data = {
            'description': faker.pystr(min_chars=1001, max_chars=1001),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_description == Distro.objects.first().description

    def test_update_logo_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_logo = distro.logo
        data = {
            'logo': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_logo == Distro.objects.first().logo

    def test_update_origin_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_origin = distro.origin
        data = {
            'origin': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_origin == Distro.objects.first().origin

    def test_update_based_on_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_based_on = distro.based_on
        data = {
            'based_on': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_based_on == Distro.objects.first().based_on

    def test_update_home_page_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_home_page = distro.home_page
        data = {
            'home_page': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_home_page == Distro.objects.first().home_page

    def test_update_user_forums_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        distro = Distro.objects.first()
        distro_detail_url = reverse('distro-detail', kwargs={'pk': distro.pk})
        distro_user_forums = distro.user_forums
        data = {
            'user_forums': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(distro_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert distro_user_forums == Distro.objects.first().user_forums
