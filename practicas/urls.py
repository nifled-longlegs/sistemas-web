from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.ciclos, name='ciclos'),

    # ex: /materia/5/
    path('materia/<int:materia_id>/', views.materia_detail, name='materia-detail'),

    # ex: /practica/5/
    path('practica/<int:practica_id>/', views.practica_detail, name='practica-detail'),
]
