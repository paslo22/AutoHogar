from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^luz/$',views.luz, name='luz'),
	url(r'^garage/$',views.garage, name='garage'),
	url(r'^termometro/$',views.termometro, name='termometro'),
]