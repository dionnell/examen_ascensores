from django.db import models

class empresa (models.Model):
	nombre = models.CharField(max_length=50, primary_key=True)
	direccion = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	comuna = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.EmailField(unique=True)
	
	def __str__(self):
		return '{}'.format(self.nombre)