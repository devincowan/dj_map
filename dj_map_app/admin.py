# from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import Point

admin.site.register(Point, LeafletGeoAdmin)
