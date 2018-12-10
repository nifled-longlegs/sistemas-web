from django.contrib import admin
from .models import Practica, Alumno, PracticaAlumno, Ciclo, Materia

# Register your models here.
admin.site.register(Ciclo)
admin.site.register(Materia)
admin.site.register(Practica)
admin.site.register(Alumno)
admin.site.register(PracticaAlumno)
