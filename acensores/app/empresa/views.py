from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.empresa.forms  import empresaForm
from app.empresa.models import empresa

def empresa_view(request):
	if request.method == 'POST':
		form = empresaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
		
	else:
		form = empresaForm()
	return render(request, 'empresa_form.html', {'form':form})

def empresa_list(request):
	Empresa = empresa.objects.all()
	contexto = {'empresas': Empresa}
	return render(request, 'empresa_list.html', contexto)

