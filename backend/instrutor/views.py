from django.http import JsonResponse
from .models import Instrutor

# Create your views here.

def listar_instrutores(request):
    instrutores=Instrutor.objects.all()
    return JsonResponse(list(instrutores.values()), safe=False)

def instrutores_ativos(request):
    instrutores=Instrutor.objects.filter(status='ativo')
    return JsonResponse(list(instrutores.values()), safe=False)

def instrutores_inativos(request):
    instrutores=Instrutor.objects.filter(status='inativo')
    return JsonResponse(list(instrutores.values()), safe=False)
