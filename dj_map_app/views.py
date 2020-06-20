from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Point
from .forms import PointForm

# Create your views here.


def index(request):
    """Index page for maps app"""
    return render(request, 'index.html')


@login_required
def large(request):
    """Page for maps"""
    return render(request, 'large.html')


@login_required
def points(request):
    """Page for points"""
    # query the points model, filter by user
    points = Point.objects.filter(owner=request.user).order_by('date_added')

    # context is a dictionary of key/vals
    context = {'points': points}
    return render(request, 'points.html', context)


@login_required
def point(request, point_id):
    """Page for single point"""
    # query the points model for matching point
    point = Point.objects.get(id=point_id)

    # make sure the point belongs to current user
    if point.owner != request.user:
        raise Http404

    # context is a dictionary of key/vals
    context = {'point': point}
    return render(request, 'point.html', context)


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
    return render(request, 'new_point.html', context)
