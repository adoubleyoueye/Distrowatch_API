from rest_framework import viewsets

from .models import Architecture, DesktopInterface, Distro
from .serializers import (
    ArchitectureSerializer,
    DesktopInterfaceSerializer,
    DistroSerializer,
)


class DistroViewSet(viewsets.ModelViewSet):
    queryset = Distro.objects.all()
    serializer_class = DistroSerializer
    permission_classes = []
    filterset_fields = ['id', 'name', 'description', 'logo', 'price', 'os_type', 'origin',
                        'based_on', 'category', 'status', 'popularity', 'home_page', 'user_forums']


class DesktopInterfaceViewSet(viewsets.ModelViewSet):
    queryset = DesktopInterface.objects.all()
    serializer_class = DesktopInterfaceSerializer
    permission_classes = []
    filterset_fields = ['id', 'name']


class ArchitectureViewSet(viewsets.ModelViewSet):
    queryset = Architecture.objects.all()
    serializer_class = ArchitectureSerializer
    permission_classes = []
    filterset_fields = ['id', 'name']
