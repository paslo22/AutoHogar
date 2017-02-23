from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import serial,time

from .models import *

# THIS DOESNT BELONG HERE
# ser = serial.Serial('/dev/ttyACM0',9600)

@login_required
def index(request,housePk):
	house = get_object_or_404(Casa, pk=housePk)
	user = request.user
	return render(request, 'web/index.html', {'house':house})

@login_required
def casas(request):
	user = request.user
	houses = Casa.objects.filter(user__username=user)
	if not houses:
		return redirect('addHouse')
	elif houses.count() == 1:
		return redirect('dispositivos')
	else:
		return render(request, 'web/casas.html', {'houses':houses})

@login_required
def addHouse(request):
	if request.method == 'GET':
		return render(request, 'web/addHouse.html')
	else:
		name = request.POST.get('name','')
		u = request.user
		user = User.objects.get(username=u)
		if name == '':
			messages.info(request, 'Nombre no puede ser vacío.')
			return render(request, 'web/addHouse.html')
		c = Casa(nombre=name, user=user)
		c.save()
		messages.info(request,'Casa creada correctamente.')
		return redirect('casas')

@csrf_exempt
def luz(request):
	id = request.POST.get('id')
	luz = get_object_or_404(Luz,pk=id)
	luz.change_state()
	return HttpResponse(request)

@csrf_exempt
def garage(request):
	id = request.POST.get('id')
	op = request.POST.get('op')
	garage = get_object_or_404(Garage, pk=id)
	garage.change_state(op)
	return HttpResponse(request)

@csrf_exempt
def termometro(request):
	id = request.GET.get('id')
	term = Termometro.objects.get(pk=id)
	term.update_state()
	return JsonResponse({'t':term.estado})
