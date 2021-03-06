from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import serial

from .models import *

# THIS DOESNT BELONG HERE
# ser = serial.Serial('/dev/ttyACM0',9600)


@login_required
def index(request, housePk):
    house = get_object_or_404(Casa, pk=housePk)
    return render(request, 'web/index.html', {
        'house': house,
        'rangeTemp': range(16, 30)
    })


@login_required
def casas(request):
    user = request.user
    houses = Casa.objects.filter(user__username=user)
    if not houses:
        return redirect('addHouse')
    elif houses.count() == 1:
        return redirect('dispositivos', housePk=houses[0].pk)
    else:
        return render(request, 'web/casas.html', {'houses': houses})


@login_required
def addHouse(request):
    if request.method == 'GET':
        return render(request, 'web/addHouse.html')
    else:
        name = request.POST.get('name', '')
        u = request.user
        user = User.objects.get(username=u)
        if name == '':
            messages.info(request, 'Nombre no puede ser vacío.')
            return render(request, 'web/addHouse.html')
        c = Casa(nombre=name, user=user)
        c.save()
        messages.info(request, 'Casa creada correctamente.')
        return redirect('casas')


@login_required
def addDev(request, housePk):
    house = get_object_or_404(Casa, pk=housePk)
    if request.method == 'GET':
        return render(request, 'web/addDev.html', {'house': house})
    elif request.method == 'POST':
        type_dev = request.POST.get('type_dev', '')
        name = request.POST.get('name', '')
        name_dev = request.POST.get('name_dev', '')
        if type_dev == 'garage':
            dev = Garage(casa=house, nombre=name,
                         nombre_disp=name_dev, estado=False)
        elif type_dev == 'light':
            dev = Luz(casa=house, nombre=name,
                      nombre_disp=name_dev, estado=False)
        elif type_dev == 'ther':
            dev = Termometro(casa=house, nombre=name,
                             nombre_disp=name_dev, estado=20)
        elif type_dev == 'aire':
            dev = Aire(casa=house, nombre=name,
                       nombre_disp=name_dev, estado=False)
        else:
            messages.info(request, 'Dispositivo no implementado aún.')
            return redirect('dispositivos', housePk=house.pk)
        dev.save()
        messages.info(request, 'Dispositivo creado correctamente.')
        return redirect('dispositivos', housePk=house.pk)
    else:
        messages.info(request, 'Operación inválida.')
        return redirect('dispositivos', housePk=house.pk)


@login_required
def addRoutine(request, housePk):
    house = get_object_or_404(Casa, pk=housePk)
    if request.method == 'GET':
        icons = ['exit_to_app', 'home', 'thumb_up', 'vpn_key', 'snooze',
                 'today', 'done', 'games', 'visibility', 'alarm_on',
                 'schedule', 'new_releases', 'done_all', 'location_on',
                 'stars', 'lock_outline', 'loop', 'info'
                 ]
        colors = ['amber', 'red', 'pink', 'purple', 'indigo', 'blue',
                  'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
                  ]
        return render(request, 'web/addRoutine.html', {
            'icons': icons,
            'colors': colors,
            'house': house,
        })
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        icono = request.POST.get('icono', '')
        routine = Rutina(casa=house, nombre=name, icono=icono, color=color)
        routine.save()
        messages.info(request, 'Rutina creada correctamente.')
        return redirect('dispositivos', housePk=house.pk)
    else:
        messages.info(request, 'Operación inválida.')
        return redirect('dispositivos', housePk=house.pk)


@login_required
def removeDev(request, housePk, devPk):
    dev = get_object_or_404(Dispositivo, pk=devPk)
    dev.delete()
    messages.info(request, 'Dispositivo borrado correctamente.')
    return redirect('dispositivos', housePk)


@csrf_exempt
def luz(request):
    id = request.POST.get('id')
    luz = get_object_or_404(Luz, pk=id)
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
    return JsonResponse({'t': term.estado})


@csrf_exempt
def tempDeseada(request):
    id = request.POST.get('id')
    tempDeseada = request.POST.get('tempDeseada')
    term = Termometro.objects.get(pk=id)
    term.sendDesired(tempDeseada)
    return HttpResponse(request)


@csrf_exempt
def runRutina(request, id):
    rutina = get_object_or_404(Rutina, pk=id)
    rutina.run()
    return HttpResponse(request)
