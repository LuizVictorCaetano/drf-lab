from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
    criada_em = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.titulo
