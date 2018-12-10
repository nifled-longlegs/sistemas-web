from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.ciclos, name='ciclos'),

    # ex: /materia/5/
    path('materia/<int:materia_id>/', views.materia_detail, name='materia-detail'),


    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
