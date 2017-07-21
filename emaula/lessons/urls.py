from django.conf.urls import url

from . import views

app_name = 'lessons'

urlpatterns = [
    url(r'^text_list/$',
        views.TextListView.as_view(),
        name='text_list'),

    # == URL Lists ==
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^link_list/$', views.LinkListView.as_view(), name='link_list'),
    url(r'^image_list/$', views.ImageListView.as_view(), name='image_list'),
    url(r'^video_list/$', views.VideoListView.as_view(), name='video_list'),
    url(r'^audio_list/$', views.AudioListView.as_view(), name='audio_list'),

    # == URL details ==
    url(r'^text/(?P<pk>[0-9]+)/$',
        views.TextDetailView.as_view(), name='text_detail'),
    url(r'^link/(?P<pk>[0-9]+)/$',
        views.LinkDetailView.as_view(), name='link_detail'),
    url(r'^image/(?P<pk>[0-9]+)/$',
        views.ImageDetailView.as_view(), name='image_detail'),
    url(r'^video/(?P<pk>[0-9]+)/$',
        views.VideoDetailView.as_view(), name='video_detail'),
    url(r'^audio/(?P<pk>[0-9]+)/$',
        views.AudioDetailView.as_view(), name='audio_detail'),
]
