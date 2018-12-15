from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.servicio.forms  import servicioForm
from app.servicio.models import servicio

def servicio_view(request):
	if request.method == 'POST':
		form = servicioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
		
	else:
		form = servicioForm()
	return render(request, 'servicio_form.html', {'form':form})

def servicio_list(request):
	Servicio = servicio.objects.all()
	contexto = {'servicio': Servicio}
	return render(request, 'servicio_list.html', contexto)