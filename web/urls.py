from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.casas, name='casas'),
	url(r'^dispositivos/(?P<housePk>[0-9]+)/$',views.index, name='dispositivos'),
	url(r'^luz/$',views.luz, name='luz'),
	url(r'^garage/$',views.garage, name='garage'),
	url(r'^termometro/$',views.termometro, name='termometro'),
	url(r'^addHouse/$',views.addHouse, name='addHouse'),
]