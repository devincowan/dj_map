# from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import Point

# admin.site.register(Point, LeafletGeoAdmin)


@admin.register(Point)
class PointAdmin(LeafletGeoAdmin):
    list_display = ('text', 'geom', 'owner', 'date_added', 'date_updated')
