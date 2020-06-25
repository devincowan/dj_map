import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Point
from .forms import PointForm
from django.core.serializers import serialize


# Create your views here.


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
