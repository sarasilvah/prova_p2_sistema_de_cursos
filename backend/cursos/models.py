from django.db import models

# Create your models here.

class Curso(models.Model):

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrutor = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo