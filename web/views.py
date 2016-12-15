from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import serial,time

from .models import *

def index(request):
	return render(request, 'web/index.html', {'disp':Dispositivo.objects.all()})

@csrf_exempt
def luz(request):
	ser = serial.Serial('/dev/ttyACM0',9600)
	id = request.POST.get('id')
	luz = Luz.objects.get(pk=id)
	time.sleep(2)
	if luz.estado:
		ser.write(b'ap')
		luz.estado = False
	else:
		ser.write(b'p')
		luz.estado = True
	luz.save()
	return HttpResponse(request)

@csrf_exempt
def garage(request):
	ser = serial.Serial('/dev/ttyACM0',9600)
	id = request.POST.get('id')
	op = request.POST.get('op')
	garage = Garage.objects.get(pk=id)
	time.sleep(2)
	if op == 'abrir':
		ser.write(b'a')
		print('abrir')
		garage.estado = True
	else:
		ser.write(b'c')
		print('cerrar')
		garage.estado = False
	garage.save()
	return HttpResponse(request)