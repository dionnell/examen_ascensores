from django import forms

from app.servicio.models import servicio


class servicioForm(forms.ModelForm):

	class Meta:
		model = servicio

		fields = [
			'folio',
			'empresa' ,
			'fecha' ,
			'horaInicio' ,
			'horaTermino',
			'IdAscensor',
			'modeloAcensor',
			'fallas',
			'reparaciones',
			'piezasCambiadas',
			'tecnico'
		]
		labels = {
			'folio':'Numero de folio',
			'empresa':'Nombre de la empresa' ,
			'fecha':'Fecha de atencion' ,
			'horaInicio':'Hora Inicio' ,
			'horaTermino':'Hora Termino',
			'IdAscensor':'Id Ascensor',
			'modeloAcensor':'Modelo Acensor',
			'fallas':'fallas del Ascensor',
			'reparaciones':'Reparaciones',
			'piezasCambiadas':'Piezas Cambiadas',
			'tecnico':'Tecnico User'
		}
		widgets = {
			'folio': forms.TextInput(),
			'empresa':forms.Select(),
			'fecha': forms.TextInput(),
			'horaInicio': forms.TextInput(),
			'horaTermino': forms.TextInput(),
			'IdAscensor': forms.TextInput(),
			'modeloAcensor':forms.TextInput() ,
			'fallas' :forms.TextInput(), 
			'reparaciones' : forms.TextInput(),
			'piezasCambiadas' : forms.TextInput(),
			'tecnico':forms.Select(),

		}