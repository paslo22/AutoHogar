from django.contrib import admin

from .models import *


class dispositivoInline(admin.StackedInline):
    model = RutinasxDispositivos


class rutina(admin.ModelAdmin):
    inlines = [
        dispositivoInline,
    ]


admin.site.register(Luz)
admin.site.register(Casa)
admin.site.register(LuzD)
admin.site.register(Garage)
admin.site.register(Termometro)
admin.site.register(Dispositivo)
admin.site.register(Rutina, rutina)
