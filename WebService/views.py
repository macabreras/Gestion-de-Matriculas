from django.shortcuts import render
from matriculas.models import Estudiante, Materia
from rest_framework import viewsets
from .serializable import EstudianteSerializable, MateriaSerializable

class EstudiantesViewSet(viewsets.ModelViewSet):
	serializer_class = EstudianteSerializable
	queryset = Estudiante.objects.all()

class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class = MateriaSerializable
	queryset = Materia.objects.filter(cupo__gt=0,cupo__lte=30)