# from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.contrib.auth.models import User

# Create your models here.


class Point(models.Model):
    """A Geo Point"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    geom = models.PointField('longitude/latitude', blank=True, null=True)
    objects = GeoManager()


def __str__(self):
    """Retrun string rep of this model"""
    return self.text
