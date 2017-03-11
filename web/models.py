from django.db import models
from django.contrib.auth.models import User

# ser = serial.Serial('/dev/ttyACM0',9600)


class Casa(models.Model):
    nombre = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.user)


class Dispositivo(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    nombre_disp = models.CharField(max_length=40)


class Luz(Dispositivo):
    estado = models.BooleanField()

    def change_state(self):
        if self.estado:
            sal = self.nombre_disp + 'a'
            self.estado = False
        else:
            sal = self.nombre_disp + 'p'
            self.estado = True
        # ser.write(bytes(sal,'utf-8'))
        self.save()

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'luz'
        verbose_name_plural = 'luces'


class LuzD(Dispositivo):
    estado = models.PositiveSmallIntegerField()

    # TODO: Change State

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'luz D'
        verbose_name_plural = 'luces D'


class Garage(Dispositivo):
    estado = models.BooleanField()

    def change_state(self, operation):
        if operation == 'abrir':
            sal = self.nombre_disp + 'a'
            self.estado = True
        else:
            sal = self.nombre_disp + 'c'
            self.estado = False
        # ser.write(bytes(sal,'utf-8'))
        self.save()

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'garage'
        verbose_name_plural = 'garage'


class Termometro(Dispositivo):
    estado = models.SmallIntegerField()

    def update_state(self):
        # ser.write(bytes(self.nombre_disp, 'utf-8'))
        # t = ser.readline()
        # self.estado = t.decode('utf-8').rstrip()
        self.save()

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'termometro'
        verbose_name_plural = 'termometros'
