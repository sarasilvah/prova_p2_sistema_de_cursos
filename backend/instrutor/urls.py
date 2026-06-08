from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_instrutores),
    path('ativos/', views.instrutores_ativos),
    path('inativos/', views.instrutores_inativos),
]