from django.shortcuts import render
from .models import Point

# Create your views here.


def index(request):
    """Index page for maps app"""
    return render(request, 'index.html')


def large(request):
    """Page for maps"""
    return render(request, 'large.html')


def points(request):
    """Page for points"""
    # query the points model
    points = Point.objects.order_by('date_added')

    # context is a dictionary of key/vals
    context = {'points': points}
    return render(request, 'points.html', context)


def point(request, point_id):
    """Page for single point"""
    # query the points model for matching point
    point = Point.objects.get(id=point_id)

    # context is a dictionary of key/vals
    context = {'point': point}
    return render(request, 'point.html', context)
