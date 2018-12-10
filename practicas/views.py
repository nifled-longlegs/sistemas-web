from django.shortcuts import render
from .models import Materia, Ciclo


def ciclos(request):
  ciclos = Ciclo.objects.all().order_by('-nombre')

  context = {'ciclos': ciclos}

  return render(request, 'practicas/ciclo_list.html', context)
