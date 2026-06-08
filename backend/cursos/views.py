from django.http import JsonResponse
from .models import Curso

def listar_cursos(request):
    cursos=Curso.objects.all()
    return JsonResponse(list(cursos.values()), safe=False)

def cursos_ativos(request):
    cursos=Curso.objects.filter(status='ativo')
    return JsonResponse(list(cursos.values()), safe=False)