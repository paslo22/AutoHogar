from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import serial,time

from .models import *

ser = serial.Serial('/dev/ttyACM0',9600)

@login_required
def index(request):
	return render(request, 'web/index.html', {'disp':Dispositivo.objects.all()})

@csrf_exempt
def luz(request):
	id = request.POST.get('id')
	luz = Luz.objects.get(pk=id)
	if luz.estado:
		sal = luz.nombDisp + 'a'
		luz.estado = False
	else:
		sal = luz.nombDisp + 'p'
		luz.estado = True
	ser.write(bytes(sal,'utf-8'))
	luz.save()
	return HttpResponse(request)

@csrf_exempt
def garage(request):
	id = request.POST.get('id')
	op = request.POST.get('op')
	garage = Garage.objects.get(pk=id)
	if op == 'abrir':
		sal = garage.nombDisp + 'a'
		garage.estado = True
	else:
		sal = garage.nombDisp + 'c'
		garage.estado = False
	ser.write(bytes(sal,'utf-8'))
	garage.save()
	return HttpResponse(request)

@csrf_exempt
def termometro(request):
	id = request.GET.get('id')
	term = Termometro.objects.get(pk=id)
	ser.write(bytes(term.nombDisp,'utf-8'))
	temperatura = ser.readline()
	term.estado = temperatura.decode('utf-8')
	term.save()
	return HttpResponse(request,{'t':term.estado})