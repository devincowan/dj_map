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
    url(r'^points.nearby/', views.nearby_points_data, name='nearby_points_data'),
    path('points/<int:point_id>', views.point, name='point'),
    path('new', views.new_point, name='new_point'),
    path('new_point_post', views.new_point_post, name='new_point_post'),
    path('delete_point_post', views.delete_point_post, name='delete_point_post'),
    path('list', views.PointList.as_view())
]
