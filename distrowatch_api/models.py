from django.db import models


class Distro(models.Model):
    LINUX = 'LINUX'
    BSD = 'BSD'
    SOLARIS = 'SOLARIS'
    OTHER_OS = 'OTHER_OS'
    OS_TYPE_CHOICES = [
        (LINUX, 'LINUX'),
        (BSD, 'BSD'),
        (SOLARIS, 'SOLARIS'),
        (OTHER_OS, 'OTHER_OS')
    ]
    DESKTOP = 'DESKTOP'
    LIVE_MEDIUM = 'LIVE_MEDIUM'
    RASPBERRY_PI = 'RASPBERRY_PI'
    FROM_RAM = 'FROM_RAM'
    CATEGORY_CHOICES = [
        (DESKTOP, 'DESKTOP'),
        (LIVE_MEDIUM, 'LIVE_MEDIUM'),
        (RASPBERRY_PI, 'RASPBERRY_PI'),
        (FROM_RAM, 'FROM_RAM')
    ]
    ACTIVE = 'ACTIVE'
    DORMANT = 'DORMANT'
    DISCONTINUED = 'DISCONTINUED'
    STATUS_CHOICES = [
        (ACTIVE, 'ACTIVE'),
        (DORMANT, 'DORMANT'),
        (DISCONTINUED, 'DISCONTINUED')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0.0)
    os_type = models.CharField(max_length=8, choices=OS_TYPE_CHOICES,
                               null=True, blank=True, default='Linux')
    origin = models.CharField(max_length=255, null=True, blank=True)
    based_on = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    home_page = models.CharField(max_length=255, null=True, blank=True)
    user_forums = models.CharField(max_length=255, null=True, blank=True)
    desktop_interfaces = models.ManyToManyField(
        'DesktopInterface', related_name='distros', db_table='distro_desktop_interface', blank=True)
    architectures = models.ManyToManyField(
        'Architecture', related_name='distros', db_table='distro_architecture', blank=True)

    class Meta:
        db_table = "distro"


class DesktopInterface(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = "desktopInterface"


class Architecture(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = "architecture"
