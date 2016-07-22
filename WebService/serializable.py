from rest_framework import serializers
from matriculas.models import Estudiante, Materia

class EstudianteSerializable(serializers.ModelSerializer):
	class Meta:
		model = Estudiante
		fields = ("cedula","nombre","apellido")

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model = Materia 
		fields = ("nombre","cupo")