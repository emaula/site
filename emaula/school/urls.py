from django.conf.urls import url

from . import views

app_name = 'school'

urlpatterns = [
    # Barra de navegação
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.home_page, name='index'),
    url(r'^about/$', views.about_project, name='about'),
    url(r'^team/$', views.team, name='team'),
    url(r'^colaborate/$', views.colaborate, name='colaborate'),
    url(r'^tos/$', views.tos, name='tos'),

    # Status do site
    url(r'^sitestatus/$', views.sitestatus, name='sitestatus'),
    url(r'^professor/$', views.ProfessorListView.as_view(), name='professor'),

    # Lista de aulas
    url(r'^classrooms/$',
        views.ClassroomListView.as_view(), name='classroom_list'),


    url(r'^professor_lessons/(?P<pk>\d+)/$',
        views.professor_lessons_list, name='professor_lessons_list'),

    url(r'^classroom/(?P<pk>\d+)$',
        views.ClassroomDetailView.as_view(), name='classroom_detail'),

    # Detalhe professor
    url(r'^professor/(?P<pk>\d+)/$',
        views.ProfessorDetailView.as_view(), name='professor_detail'),

    # Registro professor
    url(r'^register/$', views.register, name='register'),

]
