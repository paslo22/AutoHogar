from django.db import models

class Dispositivo(models.Model):
	nombre = models.CharField(max_length=40)
	nombDisp = models.CharField(max_length=40)

class Luz(Dispositivo):
	estado = models.BooleanField()

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='luz'
		verbose_name_plural='luces'

class LuzD(Dispositivo):
	estado = models.PositiveSmallIntegerField()

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='luz D'
		verbose_name_plural='luces D'

class Garage(Dispositivo):
	estado = models.BooleanField()

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='garage'
		verbose_name_plural='garage'

class Termometro(Dispositivo):
	estado = models.SmallIntegerField()

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='termometro'
		verbose_name_plural='termometros'