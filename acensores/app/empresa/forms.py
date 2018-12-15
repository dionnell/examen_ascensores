from django import forms

from app.empresa.models import empresa


class empresaForm(forms.ModelForm):

	class Meta:
		model = empresa

		fields = [
			'nombre',
			'direccion',
			'ciudad',
			'comuna',
			'telefono',
			'email',
		]
		labels = {
			'nombre': 'Nombre',
			'direccion': 'Direccion',
			'ciudad': 'Ciudad',
			'comuna':'Comuna',
			'telefono' : 'Telefono',
			'email' : 'Email',
		}
		widgets = {
			'nombre': forms.TextInput(),
			'direccion': forms.TextInput(),
			'ciudad': forms.TextInput(),
			'comuna': forms.TextInput(),
			'telefono': forms.TextInput(),
			'email': forms.EmailInput(),
		}