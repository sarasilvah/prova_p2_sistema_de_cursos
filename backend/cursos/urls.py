from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos),
    path('ativos/', views.cursos_ativos),
]