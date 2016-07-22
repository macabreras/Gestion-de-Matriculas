from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'matriculas.views.listar'),
    url(r'^NuevoEstudiante/$', 'matriculas.views.NuevoEstudiante'),
    url(r'^NuevaMateria/$', 'matriculas.views.NuevaMateria'),
    url(r'^ModificarEstudiante/$', 'matriculas.views.ModificarEstudiante'),
    url(r'^ModificarMateria/$', 'matriculas.views.ModificarMateria'),
    url(r'^EliminarEstudiante/$', 'matriculas.views.EliminarEstudiante'),
    url(r'^EliminarMateria/$', 'matriculas.views.EliminarMateria'),
]