from django.shortcuts import render, redirect
from .models import Estudiante, Materia
from .forms import FormularioEstudiante, FormularioMateria, FormularioModificarEstudiante, FormularioModificarMateria

# Create your views here.
def listar(request):
	estudiante = Estudiante.objects.all()
	materia = Materia.objects.all()
	context={
		'estudiante': estudiante,
		'materia': materia,
	}
	return render(request,"Matriculas/listar.html",context)

def NuevoEstudiante(request):
	f = FormularioEstudiante(request.POST or None)

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			e = Estudiante()
			e.cedula = f_data.get("cedula")
			e.nombre = f_data.get("nombre")
			e.apellido = f_data.get("apellido")
			if(e.save()!=True):
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"Matriculas/CrearEstudiante.html",context)

def NuevaMateria(request):
	f = FormularioMateria(request.POST or None)

	if request.method=="POST":
		if f.is_valid():
			f_data = f.cleaned_data
			m = Materia()
			m.nombre = f_data.get("nombre")
			m.cupo = f_data.get("cupo")
			if(m.save()!=True):
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"Matriculas/CrearMateria.html",context)


def ModificarEstudiante(request):
	est = Estudiante.objects.get(cedula=request.GET['cedula'])
	f = FormularioModificarEstudiante(request.POST or None)

	f.fields["nombre"].initial = est.nombre
	f.fields["apellido"].initial = est.apellido

	if f.is_valid():
		f_data = f.cleaned_data
		est.nombre = f_data.get("nombre")
		est.apellido = f_data.get("apellido")
		est.save()
		return redirect(listar)

	context = {
		'est':est,
		'f':f,
	}
	return render(request,"Matriculas/ModificarEstudiante.html",context)

def ModificarMateria(request):
	mat = Materia.objects.get(nombre=request.GET['nombre'])
	f = FormularioModificarMateria(request.POST or None)

	f.fields["cupo"].initial = mat.cupo
	if f.is_valid():
		f_data = f.cleaned_data
		mat.cupo = f_data.get("cupo")
		mat.save()
		return redirect(listar)
	context={
		'mat':mat,
		'f':f,
	}
	return render(request,"Matriculas/ModificarMateria.html",context)

def EliminarEstudiante(request):
	est = Estudiante.objects.get(cedula=request.GET['cedula'])
	est.delete()
	return redirect(listar)

def EliminarMateria(request):
	mat = Materia.objects.get(nombre=request.GET['nombre'])
	mat.delete()
	return redirect(listar)