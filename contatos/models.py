from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model): #Herdando de uma classe do Django
    nome = models.CharField(max_length=255) # caracteres com no máximo 255
    sobrenome = models.CharField(max_length=255, blank=True) # permite ficar vazio (opcional)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True) # Campo de mostrar o contato ou não, marcando como booleano.
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m') # Local onde salva as fotos, salva com o dia e o mês

    objects = models.Manager()  # Serve para deixar claro que é um objeto

    def __str__(self):
        return self.nome

