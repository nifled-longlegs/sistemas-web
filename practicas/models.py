from django.db import models


class Practica(models.Model):
  numero_practica = models.PositiveIntegerField()
  titulo = models.CharField(max_length=255)
  descripcion = models.CharField(max_length=255)
  archivo = models.FileField(upload_to='practicas/')
  fecha = models.DateField(auto_now=True)

  def __str__(self):
    return self.titulo


class Alumno(models.Model):
  name = models.CharField(max_length=85)


class PracticaAlumno(models.Model):
  practica = models.ForeignKey(Practica, on_delete=models.CASCADE)
  alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
  terminada = models.BooleanField(default=False)
  calificacion = models.PositiveIntegerField()
