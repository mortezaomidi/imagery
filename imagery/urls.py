# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (SceneListView, SceneDetailView, GeoSceneDetailView,
    cloud_rate_view, request_scene_view, SceneRequestByUserListView,
    NotFoundSceneRequestListView, SceneRequestDeleteView, GeoSceneListView)


app_name = 'imagery'

urlpatterns = [
    url(r'^$', SceneListView.as_view(), name='index'),
    url(r'^geo/$', GeoSceneListView.as_view(), name='geoscene-listview'),
    url(r'^scene/(?P<slug>\w+)/$', SceneDetailView.as_view(), name='scene'),
    url(r'^scene/(?P<name>\w+)/geo/$', GeoSceneDetailView.as_view(),
        name='geoscene'),
    url(r'^cloud-rate/$', cloud_rate_view, name='cloud-rate'),
    url(r'^request-scene/$',
        login_required(request_scene_view),
        name='request-scene'),
    url(r'^user-scene-request/$',
        login_required(SceneRequestByUserListView.as_view()),
        name='user-scene-request'),
    url(r'^not-found-scene-request/$',
        NotFoundSceneRequestListView.as_view(),
        name='not-found-scene-request'),
    url(r'^scene-request/(?P<pk>\d+)/delete/$',
        SceneRequestDeleteView.as_view(),
        name='delete-scene-request'),
]
