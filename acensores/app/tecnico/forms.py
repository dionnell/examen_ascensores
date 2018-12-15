from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class tecnicoForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
		'username',
		'first_name',
		'last_name',
		'email',
        ]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Email',
		}
		