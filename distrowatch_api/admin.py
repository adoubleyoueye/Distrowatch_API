from django.contrib import admin

from .models import Architecture, DesktopInterface, Distro

admin.site.register(Distro)
admin.site.register(DesktopInterface)
admin.site.register(Architecture)
