from django import forms
from .models import Estudiante
from .models import Materia

class FormularioEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields=["cedula","nombre","apellido"]

class FormularioMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","cupo"]


class FormularioModificarEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields=["nombre","apellido"]

class FormularioModificarMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["cupo"]