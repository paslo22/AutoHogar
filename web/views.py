from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import serial

from .models import *

def index(request):
	return render(request, 'web/index.html', {'disp':Dispositivo.objects.all()})

@csrf_exempt
def luz(request):
	#ser = serial.Serial('/dev/ttyACM0',9600)
	id = request.POST.get('id')
	luz = Luz.objects.get(pk=id)
	if luz.estado:
		ser.write('ap')
	else:
		ser.write('p')
	return HttpResponse(request)