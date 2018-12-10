from django.contrib import admin
from .models import Practica, Alumno, PracticaAlumno, Ciclo, Materia

# Register your models here.
admin.site.register(Ciclo)
admin.site.register(Materia)
admin.site.register(Practica)
admin.site.register(Alumno)
admin.site.register(PracticaAlumno)

# Admin Site Config
admin.sites.AdminSite.site_header = 'Practicas Alumnos Admin'
admin.sites.AdminSite.site_title = 'Practicas Alumnos Admin'
admin.sites.AdminSite.index_title = 'Administración'
