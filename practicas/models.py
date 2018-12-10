from django.db import models


class Practica(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  file_url = models.FileField(upload_to='practicas/')
