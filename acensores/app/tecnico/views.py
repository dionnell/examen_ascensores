from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from app.tecnico.forms import tecnicoForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.urls import reverse



def index(request):
	return render(request, 'index.html')

def login(request):
    return render(request, 'iniciosesion.html')

class registro(CreateView):
	model = User
	form_class = tecnicoForm
	template_name = "registrotecnico.html"
	success_url = reverse_lazy('index')

def user_login(request):
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	User = authenticate(username=username, password=password)
    	login(request,User)
    	return  redirect('index')
    else:
    	return render(request, 'iniciosesion.html')


