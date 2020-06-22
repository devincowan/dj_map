from django.urls import path
from django.conf.urls import url

from . import views

# app namespace
app_name = 'dj_map_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('large', views.large, name='large'),
    path('points', views.points, name='points'),
    url(r'^points.data/', views.points_data, name='points_data'),
    path('points/<int:point_id>', views.point, name='point'),
    path('new', views.new_point, name='new_point'),
]
