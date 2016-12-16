from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import serial,time

from .models import *

ser = serial.Serial('/dev/ttyACM0',9600)

def index(request):
	return render(request, 'web/index.html', {'disp':Dispositivo.objects.all()})

@csrf_exempt
def luz(request):
	id = request.POST.get('id')
	luz = Luz.objects.get(pk=id)
	time.sleep(2)
	if luz.estado:
		sal = luz.nombDisp + 'ap'
		luz.estado = False
	else:
		sal = luz.nombDisp + 'p'
		luz.estado = True
	ser.write(b'%s' % (sal))
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
		garage.estado = True
	else:
		ser.write(b'c')
		garage.estado = False
	garage.save()
	return HttpResponse(request)