from rest_framework import serializers

from .models import Architecture, DesktopInterface, Distro


class DistroSerializer(serializers.ModelSerializer):
    desktop_interfaces = serializers.PrimaryKeyRelatedField(
        queryset=DesktopInterface.objects.all(),
        many=True,
        required=False
    )
    architectures = serializers.PrimaryKeyRelatedField(
        queryset=Architecture.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Distro
        fields = ['id', 'name', 'description', 'logo', 'price', 'os_type', 'origin', 'based_on', 'category',
                  'status', 'popularity', 'home_page', 'user_forums', 'desktop_interfaces', 'architectures']


class DesktopInterfaceSerializer(serializers.ModelSerializer):
    distros = serializers.PrimaryKeyRelatedField(
        queryset=Distro.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = DesktopInterface
        fields = ['id', 'name', 'distros']


class ArchitectureSerializer(serializers.ModelSerializer):
    distros = serializers.PrimaryKeyRelatedField(
        queryset=Distro.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Architecture
        fields = ['id', 'name', 'distros']
