from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.casas, name='casas'),
    url(r'^dispositivos/(?P<housePk>[0-9]+)/$',
        views.index, name='dispositivos'),
    url(r'^luz/$', views.luz, name='luz'),
    url(r'^garage/$', views.garage, name='garage'),
    url(r'^termometro/$', views.termometro, name='termometro'),
    url(r'^addHouse/$', views.addHouse, name='addHouse'),
    url(r'^addRoutine/(?P<housePk>[0-9]+)/$',
        views.addRoutine, name='addRoutine'),
    url(r'^addDev/(?P<housePk>[0-9]+)/$', views.addDev, name='addDev'),
    url(r'^removeDev/(?P<housePk>[0-9]+)/(?P<devPk>[0-9]+)/$',
        views.removeDev, name='removeDev'),
    url(r'^tempDeseada/$', views.tempDeseada, name='tempDeseada'),
    url(r'^runRoutine/(?P<id>[0-9]+)/$',
        views.runRutina, name='runRutina'),
]
