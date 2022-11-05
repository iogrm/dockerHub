from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework import renderers
from hub.views.hub_views import HubViewSet
from hub.views.run_views import RunViewSet

app_crud = HubViewSet.as_view({
    'get': 'getAll',
    'post': 'create',
    'put': 'edit',
    'delete': 'remove',
})
app_get_all = HubViewSet.as_view({
    'get': 'get',
})
run_app = RunViewSet.as_view({
    'get': 'run',
})
runs_history = RunViewSet.as_view({
    'get': 'history',
})

urlpatterns = [
    path('app/', app_crud, name='crud_app'),
    path('app/<str:pk>/', app_get_all, name='get_all_apps'),
    path('run/<str:pk>/', run_app, name='run_app'),
    path('history/', runs_history, name='runs_history'),
]
