from django.db import models

class Pergunta(models.Model):
    texto_da_pergunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data da publicação ')

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)  #toda alternativa tem que estar vinculada a uma pergunta e Na tabela pergunta, cada pergunta vai ter um codigo, uma chave
    alternativa_text = models.CharField(max_length=200) # campo que permite escrever as alternativas possiveis
    votos = models.IntegerField(default=0)

# Create your models here.
