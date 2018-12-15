from django.db import models
from app.empresa.models import empresa
from django.contrib.auth.models import User


class servicio(models.Model):
	folio = models.CharField(max_length=10, primary_key=True)
	empresa = models.ForeignKey(empresa, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateField()
	horaInicio = models.TimeField()
	horaTermino = models.TimeField()
	IdAscensor = models.CharField(max_length=50 )
	modeloAcensor = models.CharField(max_length=50 )
	fallas = models.TextField()
	reparaciones = models.TextField()
	piezasCambiadas = models.TextField()
	tecnico = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

