from django.contrib import admin
from .models import Practica, Alumno, PracticaAlumno

# Register your models here.
admin.site.register(Practica)
admin.site.register(Alumno)
admin.site.register(PracticaAlumno)
