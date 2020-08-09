from django.conf.urls import re_path

from . import views

app_name = 'school'

urlpatterns = [
    # Barra de navegação
    # url(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^$', views.home_page, name='index'),
    re_path(r'^about/$', views.about_project, name='about'),
    re_path(r'^team/$', views.team, name='team'),
    re_path(r'^colaborate/$', views.colaborate, name='colaborate'),
    re_path(r'^tos/$', views.tos, name='tos'),

    # Status do site
    re_path(r'^sitestatus/$', views.sitestatus, name='sitestatus'),
    re_path(r'^professor/$', views.ProfessorListView.as_view(), name='professor'),

    # Lista de aulas
    re_path(r'^classrooms/$',
        views.ClassroomListView.as_view(), name='classroom_list'),


    re_path(r'^professor_lessons/(?P<pk>\d+)/$',
        views.professor_lessons_list, name='professor_lessons_list'),

    re_path(r'^classroom/(?P<pk>\d+)$',
        views.ClassroomDetailView.as_view(), name='classroom_detail'),

    # Detalhe professor
    re_path(r'^professor/(?P<pk>\d+)/$',
        views.ProfessorDetailView.as_view(), name='professor_detail'),

    # Registro professor
    re_path(r'^register/$', views.register, name='register'),

]
