from django.conf.urls import include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import ArchitectureViewSet, DesktopInterfaceViewSet, DistroViewSet


class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super(DefaultRouter, self).__init__()
        self.trailing_slash = "/?"


router = OptionalSlashRouter()

router.register(r'distro', DistroViewSet, 'distro')
router.register(r'desktop_interface', DesktopInterfaceViewSet, 'desktop_interface')
router.register(r'architecture', ArchitectureViewSet, 'architecture')

schema_view = get_schema_view(
    openapi.Info(
        title="Unofficial Distrowatch JSON API",
        default_version='v1.2',
        description="Distrowatch is JSON API which provides general information about various Linux distributions as well as other free software/open source Unix-like operating systems. Data sourced from https://distrowatch.com/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path('^', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
