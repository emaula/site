from django.conf.urls import re_path

from . import views

app_name = 'lessons'

urlpatterns = [
    re_path(r'^text_list/$',
        views.TextListView.as_view(),
        name='text_list'),

    # == URL Lists ==
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^link_list/$', views.LinkListView.as_view(), name='link_list'),
    re_path(r'^image_list/$', views.ImageListView.as_view(), name='image_list'),
    re_path(r'^video_list/$', views.VideoListView.as_view(), name='video_list'),
    re_path(r'^audio_list/$', views.AudioListView.as_view(), name='audio_list'),

    # == URL details ==
    re_path(r'^text/(?P<pk>[0-9]+)/$',
        views.TextDetailView.as_view(), name='text_detail'),
    re_path(r'^link/(?P<pk>[0-9]+)/$',
        views.LinkDetailView.as_view(), name='link_detail'),
    re_path(r'^image/(?P<pk>[0-9]+)/$',
        views.ImageDetailView.as_view(), name='image_detail'),
    re_path(r'^video/(?P<pk>[0-9]+)/$',
        views.VideoDetailView.as_view(), name='video_detail'),
    re_path(r'^audio/(?P<pk>[0-9]+)/$',
        views.AudioDetailView.as_view(), name='audio_detail'),
]
