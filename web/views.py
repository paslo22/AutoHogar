from django.shortcuts import render

from .models import *
from .helpers import *

def index(request):
	dispositivos = Dispositivo.objects.all()
	return render(request, 'web/index.html', {'group_list':grouped(dispositivos,4)})