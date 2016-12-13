from django.shortcuts import render

from .models import *

def index(request):
	return render(request, 'web/index.html', {'disp':Dispositivo.objects.all()})