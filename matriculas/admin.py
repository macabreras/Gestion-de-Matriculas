from django.contrib import admin
from .models import Estudiante, Materia

class AdminEstudiante(admin.ModelAdmin):
	list_display =["cedula","nombre","apellido"]
	class Meta:
		model = Estudiante
admin.site.register(Estudiante,AdminEstudiante)

class AdminMateria(admin.ModelAdmin):
	list_display = ["nombre","cupo"]
	class Meta:
		model = Materia
admin.site.register(Materia,AdminMateria)