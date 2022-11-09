from django.urls import path
from hub.views.hub_views import HubViewSet
from hub.views.run_views import RunViewSet

app_details = HubViewSet.as_view({
    'get': 'getApp',
    'put': 'edit',
    'delete': 'delete',
})
app_list = HubViewSet.as_view({
    'get': 'getAll',
    'post': 'create',
})
run_app = RunViewSet.as_view({
    'get': 'run',
})
runs_history = RunViewSet.as_view({
    'get': 'history',
})
prune_history = RunViewSet.as_view({
    'get': 'prune',
})

urlpatterns = [
    path('app/', app_list, name='app_list'),
    path('app/<str:pk>/', app_details, name='app_details'),
    path('run/<str:pk>/', run_app, name='run_app'),
    path('history/', runs_history, name='runs_history'),
    path('prune/', prune_history, name='prune_history'),
]
