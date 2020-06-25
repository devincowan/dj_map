import os
from django.contrib.gis import geos
from .models import Point

point_csv = os.path.abspath(os.path.join('data', 'points.csv'))


def point_load():
    """Loads some polish test data to work with call"""
    with open(point_csv) as point_file:
        for line in point_file:
            text, lon, lat = line.split(',')
            point = "POINT(%s %s)" % (lon.strip(), lat.strip())
            Point.objects.create(text=text, geom=geos.fromstr(point), owner_id='1')
            # python manage.py shell
            # >>> from dj_map_app import load
            # >>> load.point_load()
