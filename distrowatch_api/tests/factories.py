from random import randint, uniform

import factory
from factory import LazyAttribute, LazyFunction, SubFactory, fuzzy
from factory.django import DjangoModelFactory
from faker import Factory

from distrowatch_api.models import Architecture, DesktopInterface, Distro

faker = Factory.create()


class DistroFactory(DjangoModelFactory):
    class Meta:
        model = Distro

    name = LazyAttribute(lambda o: faker.text(max_nb_chars=32))
    description = LazyAttribute(lambda o: faker.text(max_nb_chars=1000))
    logo = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    price = LazyAttribute(lambda o: uniform(0, 10000))
    os_type = fuzzy.FuzzyChoice(Distro.OS_TYPE_CHOICES, getter=lambda c: c[0])
    origin = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    based_on = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    category = fuzzy.FuzzyChoice(Distro.CATEGORY_CHOICES, getter=lambda c: c[0])
    status = fuzzy.FuzzyChoice(Distro.STATUS_CHOICES, getter=lambda c: c[0])
    popularity = LazyAttribute(lambda o: randint(0, 10000))
    home_page = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    user_forums = LazyAttribute(lambda o: faker.text(max_nb_chars=255))


class DesktopInterfaceFactory(DjangoModelFactory):
    class Meta:
        model = DesktopInterface

    name = LazyAttribute(lambda o: faker.text(max_nb_chars=255))


class ArchitectureFactory(DjangoModelFactory):
    class Meta:
        model = Architecture

    name = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
