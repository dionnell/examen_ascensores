from django.db import models



def crear_usuario_perfil(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(usuario=instance)

		