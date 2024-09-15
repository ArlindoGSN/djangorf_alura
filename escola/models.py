from django.db import models

# Create your models here.


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False, max_length=30)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nome
    

class Curso(models.Model):
    
    NIVEL_CHOICES = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    
    codigo = models.CharField(max_length=10, blank=False, null=False, unique=True)
    descricao = models.TextField()
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, default='B',blank=False, null=False)
    
    def __str__(self) -> str:
        return self.descricao
    
    
class Matricula(models.Model):
    PERIODO_CHOICES = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    
    
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES, default='M', blank=False, null=False)