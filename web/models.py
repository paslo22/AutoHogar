from django.db import models

class Dispositivo(models.Model):
	nombre = models.CharField(max_length=40)

class Luz(Dispositivo):
	estado = models.BooleanField()

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='luz'
		verbose_name_plural='luces'
