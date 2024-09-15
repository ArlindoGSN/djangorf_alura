from django.db import models

# Create your models here.
'''Id
Nome
E-mail
Não pode estar em branco
CPF
Máximo de 11 caracteres
Data de Nascimento
Número de Celular
Máximo de 14 caracteres'''

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False, max_length=30)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nome
    
    