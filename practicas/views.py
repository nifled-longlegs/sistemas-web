from django.shortcuts import render
from .models import Materia, Ciclo, Practica


def ciclos(request):
  ciclos = Ciclo.objects.all().order_by('-nombre')

  context = {'ciclos': ciclos}

  return render(request, 'practicas/ciclo_list.html', context)


def materia_detail(request, materia_id):
  try:
      materia = Materia.objects.get(pk=materia_id)
  except Item.DoesNotExist:
      raise Http404('Materia no existe.')

  context = {'materia': materia}

  return render(request, 'practicas/materia.html', context)


def practica_detail(request, practica_id):
  try:
      practica = Practica.objects.get(pk=practica_id)
  except Item.DoesNotExist:
      raise Http404('Practica no existe.')

  context = {'practica': practica}

  return render(request, 'practicas/practica.html', context)
