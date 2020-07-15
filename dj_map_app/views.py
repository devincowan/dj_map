import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Point
from .forms import PointForm
from django.core.serializers import serialize

from django.views import generic
from django.contrib.gis.geos import Point as geosPoint
from django.contrib.gis.db.models.functions import Distance

# TODO: get user location form browser instead of hard-coding
# cez
longitude = -108.585930
latitude = 37.348885

# tride
# longitude = -107.812286
# latitude = 37.937492

user_location = geosPoint(longitude, latitude, srid=4326)


def index(request):
    """Index page for maps app"""
    return render(request, 'dj_map_app/index.html')


@login_required
def large(request):
    """Page for maps"""
    return render(request, 'dj_map_app/large.html')


@login_required
def points(request):
    """Page for points"""
    # query the points model, filter by user
    points = Point.objects.filter(owner=request.user).order_by('date_added')

    # context is a dictionary of key/vals
    context = {'points': points}
    return render(request, 'dj_map_app/points.html', context)


@login_required
def points_data(request):
    """API for points"""
    points_as_geojson = serialize('geojson', Point.objects.all())
    return JsonResponse(json.loads(points_as_geojson))


@login_required
def nearby_points_data(request):
    """API for points"""
    distance = Distance('geom', user_location)
    points_as_geojson = Point.objects.annotate(distance=distance).order_by('distance')[0:15]
    points_as_geojson = serialize('geojson', points_as_geojson)
    return JsonResponse(json.loads(points_as_geojson))


@login_required
def point(request, point_id):
    """Page for single point"""
    # query the points model for matching point
    point = get_object_or_404(Point, id=point_id, owner=request.user)

    # context is a dictionary of key/vals
    context = {'point': point}
    return render(request, 'dj_map_app/point.html', context)


@login_required
def new_point(request):
    """Make new single point"""
    if request.method != 'POST':
        form = PointForm()
    else:
        form = PointForm(data=request.POST)
        if form.is_valid():
            # Don't save the form until the user has been set
            new_point = form.save(commit=False)
            new_point.owner = request.user
            new_point.save()
            return redirect('dj_map_app:points')

    # Display blank/invalid form
    context = {'form': form}
    return render(request, 'dj_map_app/new_point.html', context)


@login_required
def new_point_post(request):
    """Make new single point"""
    new_point = Point()
    new_point.text = request.POST.get('text', None)
    geom = request.POST.get('geometry')
    new_point.geom = request.POST.get('geometry')
    new_point.owner = request.user
    new_point.save()
    return HttpResponse(json.dumps(geom), content_type="application/json")


@login_required
def delete_point_post(request):
    """Delete single point"""
    feature = request.POST.get('feature', None)
    query = Point.objects.get(pk=feature)
    query.delete()

    # Find the point and delete it
    return HttpResponse(json.dumps(feature), content_type="application/json")


class PointList(generic.ListView):
    model = Point
    context_object_name = 'points'
    points = Point.objects.annotate(distance=Distance('geom', user_location))
    queryset = points.order_by('distance')[0:6]
    template_name = 'dj_map_app/list.html'
